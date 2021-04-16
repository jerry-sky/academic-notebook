package com.example.devoir

import android.content.Intent
import android.graphics.drawable.Drawable
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.style.DynamicDrawableSpan
import android.view.View
import android.widget.*
import androidx.core.text.set
import androidx.core.text.toSpannable
import com.example.devoir.model.Task
import com.example.devoir.model.TaskType
import java.lang.Exception
import java.util.*

const val EDIT_TASK_OBJ = "edit task"

const val TASK_DETAILS_RETURN_OBJ = "create task"

const val CREATE_TASK_CODE = 1

const val EDIT_TASK_CODE = 2

class TaskDetailsActivity : AppCompatActivity() {

    private var chosenType: TaskType = TaskType.Other
    private lateinit var timeView: TimePicker
    private lateinit var dateView: DatePicker
    private lateinit var titleView: EditText
    private lateinit var detailsView: EditText
    private lateinit var radioGroup: RadioGroup
    private lateinit var priorityView: EditText

    private var attachDatetime = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_task_details)

        this.timeView = findViewById(R.id.task_details_time_view)
        this.dateView = findViewById(R.id.task_details_date_view)
        this.titleView = findViewById(R.id.task_details_title_view)
        this.detailsView = findViewById(R.id.task_details_description_view)
        this.priorityView = findViewById(R.id.task_details_priority_view)

        this.timeView.setIs24HourView(true)

        this.timeView.visibility = View.INVISIBLE
        this.dateView.visibility = View.INVISIBLE

        // populate the radio group
        this.radioGroup = findViewById(R.id.task_details_type_radio_view)
        for (type in enumValues<TaskType>()) {
            val radioButton = RadioButton(this)
            val icon = getDrawable(TaskType.toIcon(type))!!
            // create a spannable string with an icon
            val spannable = ("  " + getString(TaskType.toString(type))).toSpannable()
            spannable[0..1] = object : DynamicDrawableSpan() {
                override fun getDrawable(): Drawable {
                    icon.setBounds(
                        0,
                        0,
                        (24 * resources.displayMetrics.density).toInt(),
                        (24 * resources.displayMetrics.density).toInt()
                    )
                    return icon
                }
            }
            radioButton.text = spannable
            radioButton.setOnClickListener {
                this.chosenType = type
            }
            radioGroup.addView(radioButton)
        }
        // select ‘low priority’ as default value
        radioGroup.check(radioGroup.getChildAt(TaskType.toId(TaskType.Other)).id)

        // accept already existing task
        val t = this.intent.getSerializableExtra(EDIT_TASK_OBJ) as Task?
        if (t != null) {
            val headerView: TextView = findViewById(R.id.create_new_task_header_view)
            headerView.text = getString(R.string.edit_task_header)

            this.titleView.setText(t.Title)
            this.detailsView.setText(t.Description)
            this.priorityView.setText(t.Priority.toString())

            radioGroup.check(radioGroup.getChildAt(TaskType.toId(t.Type)).id)
            this.chosenType = t.Type

            val d = t.DueDate
            if (d != null) {
                this.timeView.hour = d.get(Calendar.HOUR_OF_DAY)
                this.timeView.minute = d.get(Calendar.MINUTE)
                this.dateView.updateDate(
                    d.get(Calendar.YEAR),
                    d.get(Calendar.MONTH),
                    d.get(Calendar.DAY_OF_MONTH)
                )

                // re-enable datetime picker
                this.timeView.visibility = View.VISIBLE
                this.dateView.visibility = View.VISIBLE
                this.attachDatetime = true
                val switch: Switch = findViewById(R.id.task_details_datetime_switch)
                switch.isChecked = true
            }
        }

    }

    private fun toggleDatetime() {

        var new = View.VISIBLE
        if (this.attachDatetime) {
            new = View.INVISIBLE
            this.attachDatetime = false
        } else {
            this.attachDatetime = true
        }

        this.dateView.visibility = new
        this.timeView.visibility = new

    }

    fun switchDatetime(view: View) {
        this.toggleDatetime()
    }

    fun submit(view: View) {
        // get all the form fields

        // parse them
        val title = titleView.text.toString()
        val description = detailsView.text.toString()
        val type = chosenType
        var priority = 0
        try {
            // try to parse the string and just ignore exceptions (the only exception may come from an empty string)
            priority = priorityView.text.toString().toInt()
        } catch (e: Exception) {
        }

        var datetime: Calendar? = null
        if (this.attachDatetime) {
            datetime = Calendar.getInstance()
            datetime.set(
                this.dateView.year,
                this.dateView.month,
                this.dateView.dayOfMonth,
                this.timeView.hour,
                this.timeView.minute
            )
        }

        // require the task to have at least the title (the headline)
        if (title == "") {
            // show error message
            Toast.makeText(this, getString(R.string.create_new_task_error), Toast.LENGTH_SHORT)
                .show()
            return
        }

        // create a new task
        val task = Task(title, description, type, datetime, priority)

        val data = Intent()
        data.putExtra(TASK_DETAILS_RETURN_OBJ, task)

        this.setResult(RESULT_OK, data)
        this.finish()
    }

}
