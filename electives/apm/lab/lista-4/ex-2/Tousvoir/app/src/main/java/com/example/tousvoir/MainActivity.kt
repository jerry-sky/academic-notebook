package com.example.tousvoir

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import androidx.viewpager2.adapter.FragmentStateAdapter
import androidx.viewpager2.widget.ViewPager2

const val LT = "Tousvoir21"

const val RESTORE_OPENED_DIRECTORY = "restore opened images list"

const val IMAGES_LIST_FRAGMENT = "images list fragment identifier"

class MainActivity : AppCompatActivity() {

    private lateinit var pager: ViewPager2
    private lateinit var pagerAdapter: PagerAdapter

    private lateinit var listFragment: ImagesListFragment

    private var images = emptyArray<ImageFile>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        this.pager = findViewById(R.id.pager)

        intent.flags = Intent.FLAG_ACTIVITY_REORDER_TO_FRONT

        if (savedInstanceState != null) {
            this.images =
                savedInstanceState.getSerializable(RESTORE_OPENED_DIRECTORY) as Array<ImageFile>
        }

        this.listFragment = ImagesListFragment.instantiate(this.images)
        this.refreshPagerAdapter()

    }

    override fun onResume() {
        super.onResume()
        this.listFragment.update(this.images)
    }

    private inner class PagerAdapter(
        activity: AppCompatActivity,
        private val listFragment: ImagesListFragment,
        private val files: Array<ImageFile>
    ) : FragmentStateAdapter(activity) {
        override fun getItemCount(): Int {
            return this.files.size + 1
        }

        override fun createFragment(position: Int): Fragment {
            if (position == 0) {
                return this.listFragment
            } else {
                return BigImageFragment.instantiate(this.files[position - 1])
            }
        }

    }

    private fun refreshPagerAdapter() {
        this.pagerAdapter = PagerAdapter(this, listFragment, this.images)
        this.pager.adapter = this.pagerAdapter
        this.setupListeners()
    }

    private  fun setupListeners() {
        // setup all listeners
        // image list
        this.supportFragmentManager.setFragmentResultListener(
            IMAGE_CHOSEN_LISTENER,
            this
        ) { _, bundle ->
            val imageFile = bundle.getInt(IMAGE_CHOSEN_LISTENER) as Int?
                ?: return@setFragmentResultListener
            this.onChosenImage(imageFile)
        }
        // big image fragment
        this.supportFragmentManager.setFragmentResultListener(
            BIG_IMAGE_RATING_SET,
            this
        ) { _, bundle ->
            val imageFile = bundle.getSerializable(BIG_IMAGE_NEW_VALUE) as ImageFile

            this.onImageChange(imageFile)
        }

        this.supportFragmentManager.setFragmentResultListener(
            DIRECTORY_CHOSEN_LISTENER,
            this
        ) { _, bundle ->
            this.images = bundle.getSerializable(DIRECTORY_CHOSEN_LISTENER) as Array<ImageFile>
            this.refreshPagerAdapter()
        }

    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putSerializable(RESTORE_OPENED_DIRECTORY, this.images)
    }

    private fun onChosenImage(image: Int) {
        this.pager.currentItem = 1 + image

    }

    private fun onImageChange(imageFile: ImageFile) {
        for (i in 0..this.images.size) {
            val cur = this.images[i]
            if (cur.uri == imageFile.uri) {
                // update the image
                this.images[i] = imageFile
                break
            }
        }
        this.listFragment.update(this.images)
        this.pagerAdapter.notifyDataSetChanged()
    }

    private fun resortImages() {
        this.images.sortByDescending { it.rating }
    }

    override fun onBackPressed() {
        if (this.pager.currentItem == 0) {
            super.onBackPressed()
        } else {
            this.pager.currentItem = 0
            this.resortImages()
            this.listFragment.update(this.images)
            this.refreshPagerAdapter()
        }
    }

}
