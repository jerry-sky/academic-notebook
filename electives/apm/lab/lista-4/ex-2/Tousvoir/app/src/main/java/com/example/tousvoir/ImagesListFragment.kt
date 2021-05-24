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
import android.widget.TextView
import androidx.activity.result.ActivityResult
import androidx.activity.result.contract.ActivityResultContracts
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

    private lateinit var titleView: TextView
    private lateinit var recyclerView: RecyclerView
    private var adapter: ImagesListAdapter? = null

    private var images: Array<ImageFile> = emptyArray()

    private var chooseDirectoryLauncher =
        this.registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result: ActivityResult ->
            val resultCode = result.resultCode
            val data = result.data

            if (resultCode == Activity.RESULT_OK && data != null) {

                val treeUri = data.data ?: return@registerForActivityResult

                this.openDirectory(treeUri)

            }

        }

    companion object {
        fun instantiate(files: Array<ImageFile>): ImagesListFragment {
            val fragment = ImagesListFragment()
            fragment.apply {
                arguments = Bundle().apply {
                    putSerializable(REOPEN_DIRECTORY, files)
                }
            }
            return fragment
        }
    }

    private fun openDirectory(treeUri: Uri) {
        val tree = DocumentFile.fromTreeUri(this.requireContext(), treeUri) ?: return

        this.titleView.text = treeUri.path

        var metadata: Array<ImageMetadata> = tree.listFiles()

        // filter out non-image files
        metadata = metadata.filter { FileImageTypes.contains(it.type) }.toTypedArray()

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

        this.titleView = this.requireView().findViewById(R.id.fragment_images_list_title_view)

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
        this.adapter = ImagesListAdapter(this.images, {
            val bundle = Bundle().apply {
                putInt(IMAGE_CHOSEN_LISTENER, it)
            }
            this.setFragmentResult(IMAGE_CHOSEN_LISTENER, bundle)
        }, this.requireActivity().contentResolver)
        this.recyclerView.adapter = this.adapter
    }

    private fun refreshRecyclerAdapter() {
        this.adapter?.update(this.images)
    }

    private fun onDirectoryButtonClick(view: View) {
        this.openDirectory()
    }

    private fun openDirectory() {
        val intent = Intent(Intent.ACTION_OPEN_DOCUMENT_TREE).apply {
            putExtra(DocumentsContract.EXTRA_INITIAL_URI, this@ImagesListFragment.pickerInitialUri)
        }
        this.chooseDirectoryLauncher.launch(intent)
    }

    fun update(images: Array<ImageFile>) {
        this.images = images
        this.refreshRecyclerAdapter()
    }

}
