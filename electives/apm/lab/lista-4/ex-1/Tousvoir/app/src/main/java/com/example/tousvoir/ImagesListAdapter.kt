package com.example.tousvoir

import android.content.ContentResolver
import android.media.ThumbnailUtils
import android.util.Size
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.core.net.toFile
import androidx.recyclerview.widget.RecyclerView
import java.io.File
import java.net.URI

class ImagesListAdapter(
    private var data: Array<ImageFile>,
    private val onClickListener: (image: ImageFile) -> Unit,
    private val contentResolver: ContentResolver
) : RecyclerView.Adapter<ImagesListAdapter.ImagesListElementViewHolder>() {

    class ImagesListElementViewHolder(private val view: View) : RecyclerView.ViewHolder(view) {
        val title: TextView = view.findViewById(R.id.images_list_element_title_view)
        val rating: TextView = view.findViewById(R.id.images_list_element_rating_view)
        val thumbnail: ImageView = view.findViewById(R.id.images_list_element_thumbnail_view)

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

        val thumbnail = this.contentResolver.loadThumbnail(image.uri, Size(64, 64), null)

//        val thumbnail = thumbnailutils.createimagethumbnail(file(image.uri.path), size(64, 64), null)

        holder.title.text = image.name
        holder.rating.text = image.rating.toString() + " " + holder.itemView.context.getString(R.string.stars)
        holder.thumbnail.setImageBitmap(thumbnail)

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
