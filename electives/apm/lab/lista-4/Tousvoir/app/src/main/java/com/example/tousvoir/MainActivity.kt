package com.example.tousvoir

import android.app.Activity
import android.content.Intent
import android.content.res.Configuration
import android.os.Bundle
import android.util.Log
import androidx.activity.result.ActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity

const val LT = "Tousvoir21"

const val RESTORE_OPENED_IMAGE = "restore opened image"

const val IMAGES_LIST_FRAGMENT = "images list fragment identifier"
const val BIG_IMAGE_FRAGMENT = "big image fragment identifier"

class MainActivity : AppCompatActivity() {

    private var lastImage: ImageFile? = null

    private val bigImageActivityLauncher = this.registerForActivityResult(ActivityResultContracts.StartActivityForResult()) {
            result: ActivityResult ->
        Log.i(LT, "ANY activity result")
        Log.i(LT, result.resultCode.toString())
        if(result.resultCode == Activity.RESULT_OK) {
            val data = result.data ?: return@registerForActivityResult

            this.lastImage = data.getSerializableExtra(BIG_IMAGE_NEW_VALUE) as ImageFile

            this.onImageChange(this.lastImage!!)
            Log.i(LT, "activity result")

            if(!this.isInPortrait()) {
                Log.i(LT, "activity result conditional")
                this.putUpBigImageFragment(this.lastImage!!)
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (savedInstanceState == null) {
            // initialise the fragment
            val listFragment = ImagesListFragment()

            // put up the fragment
            this.supportFragmentManager.beginTransaction().apply {
                replace(R.id.image_list_fragment, listFragment, IMAGES_LIST_FRAGMENT)
                commit()
            }
            this.supportFragmentManager.executePendingTransactions()

        } else {
            if (!this.isInPortrait()) {
                // restore last opened image
                val img = savedInstanceState.getSerializable(RESTORE_OPENED_IMAGE) as ImageFile?
                if (img != null) {
                    this.lastImage = img
                    this.putUpBigImageFragment(this.lastImage!!)
                }
            }
        }

        // setup all listeners
        // image list
        this.supportFragmentManager.setFragmentResultListener(
            IMAGE_CHOSEN_LISTENER,
            this
        ) { _, bundle ->
            val imageFile = bundle.getSerializable(IMAGE_CHOSEN_LISTENER) as ImageFile?
                ?: return@setFragmentResultListener
            this.onChosenImage(imageFile)
        }
        // big image fragment
        if (!this.isInPortrait()) {
            this.supportFragmentManager.setFragmentResultListener(
                BIG_IMAGE_RATING_SET,
                this
            ) { _, bundle ->
                val imageFile = bundle.getSerializable(BIG_IMAGE_NEW_VALUE) as ImageFile

                this.onImageChange(imageFile)
            }
        }

    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)

        outState.putSerializable(RESTORE_OPENED_IMAGE, this.lastImage)
    }

    private fun onChosenImage(image: ImageFile) {
        this.lastImage = image
        if (this.isInPortrait()) {
            val i = Intent(this, BigImageActivity::class.java)
            i.putExtra(BIG_IMAGE_ACTIVITY_IMAGE_FILE, image)
            this.bigImageActivityLauncher.launch(i)
        } else {
            this.putUpBigImageFragment(image)
        }
    }

    private fun onImageChange(imageFile: ImageFile) {
        val listFragment = supportFragmentManager.findFragmentByTag(IMAGES_LIST_FRAGMENT) as ImagesListFragment
        listFragment.updateImage(imageFile)
    }

    private fun putUpBigImageFragment(image: ImageFile) {
        val bigImageFragment = BigImageFragment.instantiate(image)
        this.supportFragmentManager.beginTransaction().apply {
            replace(R.id.big_image_fragment, bigImageFragment, BIG_IMAGE_FRAGMENT)
            commit()
        }
    }

    private fun isInPortrait(): Boolean {
        return resources.configuration.orientation == Configuration.ORIENTATION_PORTRAIT
    }

}
