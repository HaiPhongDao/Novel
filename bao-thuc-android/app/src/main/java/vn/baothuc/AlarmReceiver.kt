package vn.baothuc

import android.app.AlarmManager
import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.media.AudioAttributes
import android.media.RingtoneManager

object Alarm {
    const val CHANNEL = "baothuc"
    private const val PREFS = "baothuc"

    fun canExact(c: Context) =
        android.os.Build.VERSION.SDK_INT < 31 || c.getSystemService(AlarmManager::class.java).canScheduleExactAlarms()

    fun prefs(c: Context) = c.getSharedPreferences(PREFS, Context.MODE_PRIVATE)

    fun schedule(c: Context) {
        val p = prefs(c)
        val at = System.currentTimeMillis() + p.getInt("minutes", 20) * 60_000L
        p.edit().putBoolean("on", true).putLong("next", at).apply()
        val am = c.getSystemService(AlarmManager::class.java)
        val pi = PendingIntent.getBroadcast(
            c, 1, Intent(c, AlarmReceiver::class.java),
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
        )
        if (canExact(c)) am.setExactAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, at, pi)
        else am.setAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, at, pi)
    }

    fun cancel(c: Context) {
        prefs(c).edit().putBoolean("on", false).apply()
        val am = c.getSystemService(AlarmManager::class.java)
        am.cancel(
            PendingIntent.getBroadcast(
                c, 1, Intent(c, AlarmReceiver::class.java),
                PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
            )
        )
    }
}

class AlarmReceiver : BroadcastReceiver() {
    override fun onReceive(c: Context, i: Intent?) {
        val nm = c.getSystemService(NotificationManager::class.java)
        val sound = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_ALARM)
        nm.createNotificationChannel(
            NotificationChannel(Alarm.CHANNEL, "Báo thức lặp", NotificationManager.IMPORTANCE_HIGH).apply {
                setSound(
                    sound,
                    AudioAttributes.Builder().setUsage(AudioAttributes.USAGE_ALARM).build()
                )
                enableVibration(true)
                vibrationPattern = longArrayOf(0, 500, 250, 500, 250, 500)
            }
        )
        val open = PendingIntent.getActivity(
            c, 0, Intent(c, MainActivity::class.java),
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
        )
        nm.notify(
            1,
            Notification.Builder(c, Alarm.CHANNEL)
                .setSmallIcon(android.R.drawable.ic_lock_idle_alarm)
                .setContentTitle("Hết ${Alarm.prefs(c).getInt("minutes", 20)} phút")
                .setContentText("Chạm để mở. Báo thức tự đếm lại.")
                .setContentIntent(open)
                .setAutoCancel(true)
                .setCategory(Notification.CATEGORY_ALARM)
                .build()
        )
        Alarm.schedule(c)
    }
}
