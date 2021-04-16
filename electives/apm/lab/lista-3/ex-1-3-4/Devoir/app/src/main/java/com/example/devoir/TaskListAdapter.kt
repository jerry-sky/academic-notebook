package com.example.devoir

import android.content.Intent
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.recyclerview.widget.RecyclerView
import com.example.devoir.model.Task
import com.example.devoir.model.TaskType

class TaskListAdapter(private val data: MutableList<Task>, private val onClickListener: (task: Task, position: Int) -> Unit) :
    RecyclerView.Adapter<TaskListAdapter.TaskListViewHolder>() {

    class TaskListViewHolder(private val view: View) : RecyclerView.ViewHolder(view) {
        val title: TextView = view.findViewById(R.id.task_list_text_view)
        val date: TextView = view.findViewById(R.id.task_list_date_text_view)
        val icon: ImageView = view.findViewById(R.id.task_icon_view)

        init {
        }

        fun addListener(l: View.OnClickListener) {
            view.setOnClickListener(l)
        }
    }

    fun update() {
        this.notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): TaskListViewHolder {
        val view =
            LayoutInflater.from(parent.context).inflate(R.layout.task_list_view, parent, false)
        return TaskListViewHolder(view)
    }

    override fun onBindViewHolder(holder: TaskListViewHolder, position: Int) {
        val task = data[position]
        holder.title.text = task.Title + " (" + task.Priority + ")"
        holder.date.text = task.DueDateString()
        holder.icon.setImageResource(TaskType.toIcon(task.Type))

        holder.addListener {
            this.onClickListener(task, position)
        }
    }

    override fun getItemCount(): Int {
        return data.size
    }
}
