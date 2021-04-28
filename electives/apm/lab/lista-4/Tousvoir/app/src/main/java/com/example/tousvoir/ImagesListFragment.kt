package com.example.tousvoir

import android.app.Activity
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.provider.DocumentsContract
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.documentfile.provider.DocumentFile
import androidx.fragment.app.setFragmentResult
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

const val GET_DIRECTORY_INTENT_CODE = 1

const val IMAGE_CHOSEN_LISTENER = "images list fragment listener"
const val DIRECTORY_CHOSEN_LISTENER = "new directory opened"
const val REOPEN_DIRECTORY = "reopen directory"

class ImagesListFragment : Fragment() {

    private val pickerInitialUri = Uri.EMPTY

    private lateinit var recyclerView: RecyclerView
    private lateinit var adapter: ImagesListAdapter

    private var images: Array<ImageFile> = emptyArray()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        if (savedInstanceState != null) {
            this.images = savedInstanceState.getSerializable(REOPEN_DIRECTORY) as Array<ImageFile>?
                ?: emptyArray()
        }
    }

    override fun onViewStateRestored(savedInstanceState: Bundle?) {
        super.onViewStateRestored(savedInstanceState)

        if (savedInstanceState != null) {
            this.images = savedInstanceState.getSerializable(REOPEN_DIRECTORY) as Array<ImageFile>?
                ?: emptyArray()
        }
    }

    override fun onSaveInstanceState(outState: Bundle) {
        outState.run {
            putSerializable(REOPEN_DIRECTORY, images)
        }

        super.onSaveInstanceState(outState)
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_images_list, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        this.setupRecycler()

        val directoryButton =
            this.requireView().findViewById<Button>(R.id.open_directory_button_view)
        directoryButton.setOnClickListener(this::onDirectoryButtonClick)

        this.refreshRecyclerAdapter()
    }

    private fun setupRecycler() {
        this.recyclerView = this.requireView().findViewById(R.id.image_list_recycler_view)
        this.recyclerView.layoutManager = LinearLayoutManager(
            context,
            LinearLayoutManager.VERTICAL,
            false
        )
        this.adapter = ImagesListAdapter(this.images) {
            val bundle = Bundle().apply {
                putSerializable(IMAGE_CHOSEN_LISTENER, it)
            }
            this.setFragmentResult(IMAGE_CHOSEN_LISTENER, bundle)
        }
        this.recyclerView.adapter = this.adapter
    }

    private fun refreshRecyclerAdapter() {
        this.adapter.update(this.images)
    }

    private fun onDirectoryButtonClick(view: View) {
        this.openDirectory()
    }

    private fun openDirectory() {
        val intent = Intent(Intent.ACTION_OPEN_DOCUMENT_TREE).apply {
            putExtra(DocumentsContract.EXTRA_INITIAL_URI, this@ImagesListFragment.pickerInitialUri)
        }

        startActivityForResult(intent, GET_DIRECTORY_INTENT_CODE)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if (requestCode == GET_DIRECTORY_INTENT_CODE && resultCode == Activity.RESULT_OK && data != null) {

            val treeUri = data.data ?: return

            val tree = DocumentFile.fromTreeUri(this.requireContext(), treeUri) ?: return

            val metadata: Array<ImageMetadata> = tree.listFiles()

            val files = Array(metadata.size) {
                ImageFile(metadata[it])
            }

            this.images = files

            val bundle = Bundle().apply {
                putSerializable(DIRECTORY_CHOSEN_LISTENER, files)
            }
            this.setFragmentResult(DIRECTORY_CHOSEN_LISTENER, bundle)

            this.refreshRecyclerAdapter()

        }

    }

    fun updateImage(newImage: ImageFile) {
        // find the image that needs updating
        for(i in 0..this.images.size) {
            val cur = this.images[i]
            if(cur.uri == newImage.uri) {
                // update the image
                this.images[i] = newImage
                this.resortImages()
                this.refreshRecyclerAdapter()
                return
            }
        }
    }

    fun resortImages() {
        this.images.sortByDescending { it.rating }
    }

}
