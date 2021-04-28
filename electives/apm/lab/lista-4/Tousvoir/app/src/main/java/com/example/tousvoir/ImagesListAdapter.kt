package com.example.tousvoir

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class ImagesListAdapter(
    private var data: Array<ImageFile>,
    private val onClickListener: (image: ImageFile) -> Unit
) : RecyclerView.Adapter<ImagesListAdapter.ImagesListElementViewHolder>() {

    class ImagesListElementViewHolder(private val view: View) : RecyclerView.ViewHolder(view) {
        val title: TextView = view.findViewById(R.id.images_list_element_title_view)
        val rating: TextView = view.findViewById(R.id.images_list_element_rating_view)

        fun addListener(l: View.OnClickListener) {
            view.setOnClickListener(l)
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ImagesListElementViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.fragment_images_list_element, parent, false)
        return ImagesListElementViewHolder(view)
    }

    override fun onBindViewHolder(holder: ImagesListElementViewHolder, position: Int) {
        val image = this.data[position]
        holder.title.text = image.name
        holder.rating.text = image.rating.toString() + " " + holder.itemView.context.getString(R.string.stars)

        holder.addListener {
            this.onClickListener(image)
        }
    }

    override fun getItemCount(): Int {
        return this.data.size
    }

    fun update(data: Array<ImageFile>) {
        this.data = data
        this.notifyDataSetChanged()
    }
}
