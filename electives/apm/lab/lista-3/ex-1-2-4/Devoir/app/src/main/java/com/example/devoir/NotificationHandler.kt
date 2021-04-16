package com.example.devoir

import android.app.*
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.os.SystemClock
import android.util.Log
import androidx.core.app.NotificationCompat
import java.util.*

const val NOTIFICATION_ID = "notification id"
const val NOTIFICATION = "notification"

class NotificationHandler(
    name: String,
    descriptionText: String,
    importance: Int,
    notificationManager: NotificationManager
) {

    init {
        val channel = NotificationChannel(NOTIFICATION_CHANNEL_ID, name, importance).apply {
            description = descriptionText
        }
        notificationManager.createNotificationChannel(channel)
    }

    fun scheduleNotification(
        context: Context,
        title: String,
        content: String,
        targetTime: Calendar
    ): Int {
        val notificationId = (Calendar.getInstance().timeInMillis / 1000).toInt()
        val builder = NotificationCompat.Builder(context, NOTIFICATION_CHANNEL_ID)
            .setSmallIcon(R.drawable.notification_icon)
            .setContentTitle(title)
            .setContentText(content)
            .setStyle(
                NotificationCompat.BigTextStyle()
                    .bigText(content)
            )
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)

        val intent = Intent(context, MainActivity::class.java)
        val activity = PendingIntent.getActivity(
            context,
            notificationId,
            intent,
            PendingIntent.FLAG_CANCEL_CURRENT
        )
        builder.setContentIntent(activity)

        val notification = builder.build()

        val notificationIntent = Intent(context, NotificationPublisher::class.java)
        notificationIntent.putExtra(NOTIFICATION_ID, notificationId)
        notificationIntent.putExtra(NOTIFICATION, notification)
        val pendingIntent = PendingIntent.getBroadcast(
            context,
            notificationId,
            notificationIntent,
            PendingIntent.FLAG_CANCEL_CURRENT
        )

        val difference = targetTime.timeInMillis - Calendar.getInstance().timeInMillis
        val datetimeInMillis = SystemClock.elapsedRealtime() + difference
        val alarmManager = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        alarmManager.set(AlarmManager.ELAPSED_REALTIME, datetimeInMillis, pendingIntent)

        return notificationId
    }

    fun cancelNotification(context: Context, notificationId: Int) {
        val alarmManager = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val intent = Intent(context, NotificationPublisher::class.java)
        val pendingIntent = PendingIntent.getBroadcast(
            context,
            notificationId,
            intent,
            PendingIntent.FLAG_CANCEL_CURRENT
        )

        alarmManager.cancel(pendingIntent)
    }
}

class NotificationPublisher : BroadcastReceiver() {

    override fun onReceive(context: Context?, intent: Intent?) {

        if (context != null && intent != null) {

            val notificationManager =
                context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager

            val notification: Notification = intent.getParcelableExtra(NOTIFICATION)!!
            val notificationId = intent.getIntExtra(NOTIFICATION_ID, 0)
            notificationManager.notify(notificationId, notification)

        }

    }

}
