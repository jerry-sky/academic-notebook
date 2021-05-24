package com.example.tousvoir

import android.graphics.BitmapFactory
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.RatingBar
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.fragment.app.setFragmentResult
import java.text.DateFormat
import java.util.*

const val BIG_IMAGE_FRAGMENT_IMAGE_FILE = "big image fragment image file data"

const val BIG_IMAGE_RATING_SET = "new rating for an image was set"
const val BIG_IMAGE_NEW_VALUE = "new image value"

class BigImageFragment : Fragment() {

    private lateinit var imageView: ImageView
    private lateinit var imageDescriptionView: TextView

    private lateinit var imageFile: ImageFile

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        this.imageFile = arguments?.getSerializable(BIG_IMAGE_FRAGMENT_IMAGE_FILE) as ImageFile
    }

    companion object {
        fun instantiate(imageFile: ImageFile): BigImageFragment {
            return BigImageFragment().apply {
                arguments = Bundle().apply {
                    putSerializable(BIG_IMAGE_FRAGMENT_IMAGE_FILE, imageFile)
                }
            }
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_big_image, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        this.setupImage()
        this.setupImageDescription()
        this.setupRatingBar()
    }

    private fun setupImage() {
        this.imageView = requireView().findViewById(R.id.big_image_image_view)

        val img = this.imageFile
        // get the actual file
        val parcelFileDescriptor =
            (this.activity ?: return).contentResolver.openFileDescriptor(img.uri, "r") ?: return
        val fileDescriptor = parcelFileDescriptor.fileDescriptor
        // extract image data
        val bitmap = BitmapFactory.decodeFileDescriptor(fileDescriptor)
        parcelFileDescriptor.close()

        // put it up
        imageView.setImageBitmap(bitmap)
    }

    private fun setupImageDescription() {
        this.imageDescriptionView = requireView().findViewById(R.id.image_description_view)

        val img = this.imageFile

        val cal = Calendar.getInstance()
        cal.timeInMillis = img.lastModified

        val format = DateFormat.getDateTimeInstance(
            DateFormat.DEFAULT,
            DateFormat.SHORT,
            Locale.getDefault()
        )

        // compose the description
        var description = ""

        // image location
        description += getString(R.string.image_location)
        description += " "
        description += img.uri.path
        description += "\n\n"
        description += getString(R.string.image_last_modified)
        description += ": "
        description += format.format(cal.time)

        this.imageDescriptionView.text = description
    }

    private fun setupRatingBar() {
        val ratingBar = requireView().findViewById<RatingBar>(R.id.image_rating_view)

        ratingBar.rating = this.imageFile.rating.toFloat()

        ratingBar.setOnRatingBarChangeListener { _, rating, _ ->
            val discreteRating = rating.toInt()

            imageFile.rating = discreteRating

            val bundle = Bundle().apply {
                putSerializable(BIG_IMAGE_NEW_VALUE, imageFile)
            }

            this.setFragmentResult(BIG_IMAGE_RATING_SET, bundle)
        }
    }

}
