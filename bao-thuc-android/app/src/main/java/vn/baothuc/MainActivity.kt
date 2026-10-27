package vn.baothuc

import android.Manifest
import android.app.Activity
import android.content.Intent
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.provider.Settings
import android.text.InputType
import android.view.Gravity
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import java.util.Locale

class MainActivity : Activity() {
    private lateinit var clock: TextView
    private lateinit var info: TextView
    private lateinit var minutes: EditText
    private lateinit var button: Button
    private val handler = Handler(Looper.getMainLooper())
    private val ticker = object : Runnable {
        override fun run() { refresh(); handler.postDelayed(this, 500) }
    }

    override fun onCreate(b: Bundle?) {
        super.onCreate(b)
        val pad = (24 * resources.displayMetrics.density).toInt()
        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            gravity = Gravity.CENTER
            setPadding(pad, pad, pad, pad)
        }
        clock = TextView(this).apply { textSize = 72f; gravity = Gravity.CENTER }
        info = TextView(this).apply { textSize = 16f; gravity = Gravity.CENTER }
        minutes = EditText(this).apply {
            inputType = InputType.TYPE_CLASS_NUMBER
            gravity = Gravity.CENTER
            setText(Alarm.prefs(this@MainActivity).getInt("minutes", 20).toString())
        }
        val label = TextView(this).apply { text = "phút một lần"; gravity = Gravity.CENTER }
        button = Button(this).apply { textSize = 18f; setOnClickListener { toggle() } }
        listOf(clock, info, minutes, label, button).forEach { root.addView(it) }
        setContentView(root)
        if (Build.VERSION.SDK_INT >= 33) requestPermissions(arrayOf(Manifest.permission.POST_NOTIFICATIONS), 1)
    }

    private fun toggle() {
        val p = Alarm.prefs(this)
        if (p.getBoolean("on", false)) {
            Alarm.cancel(this)
        } else {
            val m = (minutes.text.toString().toIntOrNull() ?: 20).coerceIn(1, 600)
            p.edit().putInt("minutes", m).apply()
            minutes.setText(m.toString())
            if (Build.VERSION.SDK_INT >= 31 && !Alarm.canExact(this)) {
                startActivity(Intent(Settings.ACTION_REQUEST_SCHEDULE_EXACT_ALARM, Uri.parse("package:$packageName")))
            }
            Alarm.schedule(this)
        }
        refresh()
    }

    private fun refresh() {
        val p = Alarm.prefs(this)
        val on = p.getBoolean("on", false)
        button.text = if (on) "Dừng" else "Bắt đầu"
        minutes.isEnabled = !on
        if (on) {
            val s = ((p.getLong("next", 0) - System.currentTimeMillis()) / 1000).coerceAtLeast(0)
            clock.text = String.format(Locale.US, "%02d:%02d", s / 60, s % 60)
            info.text = "Đang chạy, lặp mỗi ${p.getInt("minutes", 20)} phút"
        } else {
            clock.text = String.format(Locale.US, "%02d:00", p.getInt("minutes", 20))
            info.text = "Chưa chạy"
        }
    }

    override fun onResume() { super.onResume(); handler.post(ticker) }
    override fun onPause() { super.onPause(); handler.removeCallbacks(ticker) }
}
