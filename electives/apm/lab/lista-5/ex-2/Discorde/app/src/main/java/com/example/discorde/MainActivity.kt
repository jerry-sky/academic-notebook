package com.example.discorde

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.firebase.ui.auth.AuthUI
import com.firebase.ui.auth.IdpResponse
import com.google.firebase.auth.ktx.auth
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.ValueEventListener
import com.google.firebase.database.ktx.database
import com.google.firebase.database.ktx.getValue
import com.google.firebase.ktx.Firebase

const val LT = "discorde2021"

const val RC_SIGN_IN = 123

class MainActivity : AppCompatActivity() {

    private val auth = Firebase.auth

    private val database = Firebase.database(FIREBASE_REALTIME_REF).reference
    private val messages = database.child(FRB_MESSAGES_REF)

    private lateinit var recyclerView: RecyclerView
    private lateinit var recyclerAdapter: MessagesAdapter

    private lateinit var messageInputView: EditText
    private lateinit var sendButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        recyclerView = findViewById(R.id.recycler)
        val layout = LinearLayoutManager(this)
        layout.orientation = LinearLayoutManager.VERTICAL
        layout.reverseLayout = true
        recyclerView.layoutManager = layout
    }

    override fun onResume() {
        super.onResume()

        val currentUser = auth.currentUser
        if (currentUser == null) {
            // need to sign in
            signIn()
        } else {
            setupMessages()
        }
    }

    private fun signIn() {
        val providers = arrayListOf(
            AuthUI.IdpConfig.EmailBuilder().build()
        )

        startActivityForResult(
            AuthUI.getInstance()
                .createSignInIntentBuilder()
                .setAvailableProviders(providers)
                .build(),
            RC_SIGN_IN
        )
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if (requestCode == RC_SIGN_IN) {
            val response = IdpResponse.fromResultIntent(data)

            if (resultCode == Activity.RESULT_OK) {
                // Successfully signed in
                setupMessages()
            } else {
                // Sign in failed. If response is null the user canceled the
                // sign-in flow using the back button. Otherwise check
                // response.getError().getErrorCode() and handle the error.
                // ...
                Log.d(LT, response?.error?.errorCode.toString())
            }
        }
    }

    private fun setupMessages() {
        recyclerAdapter = MessagesAdapter(
            emptyList(),
            auth.currentUser!!.uid,
            this::color
        )
        recyclerView.adapter = recyclerAdapter

        messageInputView = findViewById(R.id.edit_text_view)
        sendButton = findViewById(R.id.send_button)
        sendButton.setOnClickListener {
            val messageContents = messageInputView.text.toString()
            if (messageContents == "") return@setOnClickListener
            val user = auth.currentUser!!
            messages.push().setValue(
                Message(
                    messageContents,
                    user.displayName.toString(),
                    user.uid
                )
            )
            messageInputView.text = null
        }
        val msgs = messages.limitToLast(20)
        msgs.addValueEventListener(object : ValueEventListener {
            override fun onDataChange(snapshot: DataSnapshot) {
                val value = snapshot.children
                val list = value.map {
                    it.getValue<Message>()!!
                }
                recyclerAdapter.update(list)
                recyclerView.scrollToPosition(0)
            }

            override fun onCancelled(error: DatabaseError) {
                Log.e(LT, "failed to load", error.toException())
            }
        })

    }

    private fun color(id: Int): Int {
        return resources.getColor(id, theme)
    }

    class MessagesAdapter(
        private var data: List<Message>,
        private val uid: String,
        private val color: (Int) -> Int,
    ) :
        RecyclerView.Adapter<MessagesAdapter.ViewHolder>() {
        class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
            val messageView: TextView = view.findViewById(R.id.message_view)
            val usernameView: TextView = view.findViewById(R.id.username_view)
        }

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
            val view = LayoutInflater.from(parent.context)
                .inflate(R.layout.message_element, parent, false)
            return ViewHolder(view)
        }

        override fun onBindViewHolder(holder: ViewHolder, position: Int) {
            val message = data[position]

            if (message.uid == uid) {
                holder.messageView.textAlignment = TextView.TEXT_ALIGNMENT_TEXT_END
                holder.messageView.setBackgroundResource(R.color.design_default_color_primary)
                holder.messageView.setTextColor(color(R.color.design_default_color_on_primary))
            } else {
                holder.messageView.textAlignment = TextView.TEXT_ALIGNMENT_TEXT_START
                holder.messageView.setBackgroundResource(R.color.design_default_color_secondary)
                holder.messageView.setTextColor(color(R.color.design_default_color_on_secondary))
            }

            holder.messageView.text = message.contents
            holder.usernameView.text = message.author
        }

        override fun getItemCount(): Int {
            return data.size
        }

        fun update(d: List<Message>) {
            this.data = d.reversed()
            this.notifyDataSetChanged()
        }
    }
}
