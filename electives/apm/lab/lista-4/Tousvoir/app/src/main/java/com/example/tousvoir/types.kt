package com.example.tousvoir

import android.net.Uri
import androidx.documentfile.provider.DocumentFile
import java.io.Serializable

typealias ImageMetadata = DocumentFile

class ImageFile(metadata: ImageMetadata, rating: Int = 0) : Serializable {

    private val rawUri = metadata.uri.toString()

    val uri: Uri
        get() {
            return Uri.parse(this.rawUri)
        }

    val name = metadata.name ?: "untitled file"

    val lastModified = metadata.lastModified()

    var rating: Int = rating

}

val FileImageTypes = arrayOf("image/jpeg", "image/bmp", "image/gif", "image/jpg", "image/png")
