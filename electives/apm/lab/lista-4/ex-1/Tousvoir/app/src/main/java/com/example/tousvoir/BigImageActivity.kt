package com.example.tousvoir

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.PersistableBundle
import android.util.Log

const val BIG_IMAGE_ACTIVITY_IMAGE_FILE = "big image activity metadata"

const val BIG_IMAGE_NEW_VALUE_ACTIVITY = "big image activity wrapper new image value"

class BigImageActivity : AppCompatActivity() {

    private var imageFile: ImageFile? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_big_image)

        val restoredImageFile = savedInstanceState?.getSerializable(BIG_IMAGE_NEW_VALUE_ACTIVITY) as ImageFile?
        if(restoredImageFile != null) {
            this.imageFile = restoredImageFile
            this.customSetResult()
        }

        this.setupFragment()
    }

    private fun setupFragment() {
        val image = intent.getSerializableExtra(BIG_IMAGE_ACTIVITY_IMAGE_FILE) as ImageFile? ?: return
        this.supportFragmentManager.beginTransaction().apply {
            replace(R.id.big_image_fragment_external_activity, BigImageFragment.instantiate(image))
            commit()
        }

        this.supportFragmentManager.setFragmentResultListener(BIG_IMAGE_RATING_SET, this) { _, bundle ->
            this.imageFile = bundle.getSerializable(BIG_IMAGE_NEW_VALUE) as ImageFile

            this.customSetResult()
        }
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)

        if (this.imageFile != null) {
            outState.putSerializable(BIG_IMAGE_NEW_VALUE_ACTIVITY, this.imageFile)
        }
    }

    private fun customSetResult() {
        this.setResult(Activity.RESULT_OK, Intent().apply { putExtra(BIG_IMAGE_NEW_VALUE, imageFile) })
    }

}
