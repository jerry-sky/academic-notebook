package com.example.devoir.model

import com.example.devoir.R
import java.io.Serializable
import java.util.*

enum class TaskType {
    Work,
    Personal,
    Other;

    companion object {
        fun toIcon(t: TaskType): Int {
            return when (t) {
                Work -> R.drawable.task_type_work
                Personal -> R.drawable.task_type_personal
                Other -> R.drawable.task_type_other
            }
        }

        fun toString(t: TaskType): Int {
            return when (t) {
                Work -> R.string.task_type_work
                Personal -> R.string.task_type_personal
                Other -> R.string.task_type_other
            }
        }

        fun toEnum(t: Int): TaskType {
            return when (t) {
                R.string.task_type_work -> Work
                R.string.task_type_personal -> Personal
                R.string.task_type_other -> Other
                else -> Other
            }
        }

        fun toId(t: TaskType): Int {
            return when(t) {
                Work -> 0
                Personal -> 1
                Other -> 2
            }
        }
    }
}

class Task(title: String, description: String, taskType: TaskType, dueDate: Calendar?, priority: Int = 0) : Serializable {

    var Title: String = title
        private set

    var Description: String = description
        private set

    var Type: TaskType = taskType
        private set

    var DueDate: Calendar? = dueDate
        private set

    var Priority: Int = priority
        private set

    var NotificationId: Int? = null

    fun DueDateString(): String? {
        val d = this.DueDate
        return if (d != null) {
            val year = d.get(Calendar.YEAR).toString()
            val month = d.get(Calendar.MONTH).toString().padStart(2, '0')
            val day = d.get(Calendar.DAY_OF_MONTH).toString().padStart(2, '0')
            val hour = d.get(Calendar.HOUR_OF_DAY).toString().padStart(2, '0')
            val minute = d.get(Calendar.MINUTE).toString().padStart(2, '0')

            "$year-$month-$day $hour:$minute"
        } else {
            null
        }
    }

}
