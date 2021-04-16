package com.example.devoir.model

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey
import java.util.*

@Entity
data class TaskEntity(
    @PrimaryKey val uid: Int,
    val Title: String,
    val Description: String,
    val Type: TaskType,
    val DueDate: Calendar?,
    val Priority: Int,
    val NotificationId: Int?
)
