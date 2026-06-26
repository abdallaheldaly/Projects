package com.example.project_0

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.AutoCompleteTextView
import android.widget.Button
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity(), View.OnClickListener {

    lateinit var editText : EditText
    lateinit var editText1 : EditText
    lateinit var textView: TextView
    lateinit var btn : Button


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        editText = findViewById(R.id.editTextTextPersonName)
        editText1 = findViewById(R.id.editTextTextPersonName3)
        textView = findViewById(R.id.textView)
        btn = findViewById(R.id.Button)
        btn.setOnClickListener(this)
    }

    override fun onClick(p0: View?) {
        var firstname = editText.text
        var lastname = editText1.text
        textView.text = "$firstname $lastname"
    }

}