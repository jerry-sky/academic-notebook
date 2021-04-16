package com.example.devoir

import android.app.AlertDialog
import android.app.Dialog
import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import android.content.DialogInterface
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat
import androidx.fragment.app.DialogFragment
import androidx.recyclerview.widget.*
import com.example.devoir.model.Task
import com.example.devoir.model.TaskType
import java.util.*
import kotlin.collections.ArrayList

const val TASK_DETAILS = "task details"

const val NOTIFICATION_CHANNEL_ID = "devoir notifications"

class MainActivity : AppCompatActivity() {

    private lateinit var recyclerView: RecyclerView
    private var tasks: MutableList<Task> = ArrayList()
    private lateinit var recyclerAdapter: TaskListAdapter
    private lateinit var notificationHandler: NotificationHandler

    private var editTaskId = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        this.recyclerView = findViewById(R.id.recycler)
        this.setupRecycler()
        this.setupNotifications()
    }

    private fun setupNotifications() {
        this.notificationHandler = NotificationHandler(
            getString(R.string.channel_name),
            getString(R.string.channel_description),
            NotificationManager.IMPORTANCE_DEFAULT,
            getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        )
    }

    private fun setupRecycler() {
        recyclerView.layoutManager = LinearLayoutManager(
            this,
            LinearLayoutManager.VERTICAL,
            false
        )

        this.refreshRecyclerAdapter()
        val helper: SnapHelper = LinearSnapHelper()
        helper.attachToRecyclerView(recyclerView)

        val simpleItemTouchCallback: ItemTouchHelper.SimpleCallback = object :
            ItemTouchHelper.SimpleCallback(0, ItemTouchHelper.LEFT or ItemTouchHelper.RIGHT) {
            override fun onMove(
                recyclerView: RecyclerView,
                viewHolder: RecyclerView.ViewHolder,
                target: RecyclerView.ViewHolder
            ): Boolean {
                return false
            }

            override fun onSwiped(viewHolder: RecyclerView.ViewHolder, swipeDir: Int) {
                val position = viewHolder.adapterPosition
                this@MainActivity.tasks.removeAt(position)
                this@MainActivity.recyclerAdapter.update()
            }
        }
        val itemTouchHelper = ItemTouchHelper(simpleItemTouchCallback)
        itemTouchHelper.attachToRecyclerView(recyclerView)
    }

    /**
     * Overwrites current `RecyclerView` adapter with a new one.
     *
     * This way, after the refresh the adapter will also refresh the pointer to the list of tasks.
     */
    private fun refreshRecyclerAdapter() {
        fun onClickListener(task: Task, position: Int) {
            this.editTaskId = position
            val i = Intent(this, TaskDetailsActivity::class.java)
            i.putExtra(EDIT_TASK_OBJ, task)
            this.startActivityForResult(i, EDIT_TASK_CODE)
        }
        this.recyclerAdapter = TaskListAdapter(this.tasks, ::onClickListener)
        recyclerView.adapter = this.recyclerAdapter
    }

    fun createNewTask(view: View) {
        val intent = Intent(this, TaskDetailsActivity::class.java)
        this.startActivityForResult(intent, CREATE_TASK_CODE)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if (requestCode == CREATE_TASK_CODE && resultCode == RESULT_OK && data != null) {
            val task = data.getSerializableExtra(TASK_DETAILS_RETURN_OBJ) as Task
            this.tasks.add(task)
            this.recyclerAdapter.update()
            // setup notification if due date was set
            if (task.DueDate != null) {
                val targetNotificationTime: Calendar = task.DueDate!!.clone() as Calendar
                // add one day notification
                targetNotificationTime.set(
                    Calendar.DAY_OF_MONTH,
                    targetNotificationTime.get(Calendar.DAY_OF_MONTH) - 1
                )
                val notificationId = this.notificationHandler.scheduleNotification(
                    this,
                    task.Title,
                    task.Description,
                    targetNotificationTime
                )
                task.NotificationId = notificationId
            }
        } else if (requestCode == EDIT_TASK_CODE && resultCode == RESULT_OK && data != null) {
            val task = data.getSerializableExtra(TASK_DETAILS_RETURN_OBJ) as Task
            this.tasks[this.editTaskId] = task
            this.recyclerAdapter.update()

            // cancel previous notification if there was one already set up
            if (task.NotificationId != null) {
                this.notificationHandler.cancelNotification(this, task.NotificationId!!)
            }
            // if new (or the same) due date was set up, create new notification
            if(task.DueDate != null) {
                val targetNotificationTime: Calendar = task.DueDate!!.clone() as Calendar
                // add one day notification
                targetNotificationTime.set(
                    Calendar.DAY_OF_MONTH,
                    targetNotificationTime.get(Calendar.DAY_OF_MONTH) - 1
                )
                val notificationId = this.notificationHandler.scheduleNotification(
                    this,
                    task.Title,
                    task.Description,
                    targetNotificationTime
                )
                task.NotificationId = notificationId
            }
        }
    }

    override fun onSaveInstanceState(outState: Bundle) {
        outState.run {
            putSerializable(TASKS_LIST, ArrayList<Task>(this@MainActivity.tasks.toList()))
        }
        super.onSaveInstanceState(outState)
    }

    override fun onRestoreInstanceState(savedInstanceState: Bundle) {
        super.onRestoreInstanceState(savedInstanceState)

        savedInstanceState.run {
            val list = getSerializable(TASKS_LIST) as MutableList<Task>
            this@MainActivity.tasks = list
            this@MainActivity.refreshRecyclerAdapter()
        }
    }

    companion object {
        const val TASKS_LIST = "list of tasks"
    }

    fun sort(view: View) {
        fun listener(position: Int) {
            when (position) {
                0 -> {
                    this.tasks.sortBy { it.DueDate }
                }
                1 -> {
                    this.tasks.sortBy { it.Type }
                }
                2 -> {
                    this.tasks.sortByDescending { it.Priority }
                }
            }
            this.recyclerAdapter.update()
        }

        val dialog = ChooseSortingMethodDialog(::listener)
        dialog.show(supportFragmentManager, "")
    }

    class ChooseSortingMethodDialog(private val listener: (position: Int) -> Unit) :
        DialogFragment() {
        override fun onCreateDialog(savedInstanceState: Bundle?): Dialog {
            return activity.let {
                val builder = AlertDialog.Builder(it)
                builder
                    .setTitle(R.string.sort_by)
                    .setItems(R.array.sort_by, DialogInterface.OnClickListener { _, which ->
                        this.listener(which)
                    })
                builder.create()
            }
        }
    }

}
