package com.example.project_1

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity() {

    lateinit var editText_0 : EditText
    lateinit var editText_1 : EditText
    lateinit var  textView_0 : TextView
    lateinit var  textView_1: TextView
    lateinit var but_0 : Button
    lateinit var but_1 : Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        editText_0 = findViewById(R.id.first_Name_0)
        editText_1 = findViewById(R.id.Last_Name_0)
        textView_0 = findViewById(R.id.textView_0)
        textView_1 = findViewById(R.id.textView_1)
        but_0 = findViewById(R.id.button_0)
        but_1 = findViewById(R.id.button_1)

        but_0.setOnClickListener {
            var first_Name_0 = editText_0.text
            textView_0.text = "This is but_0 $first_Name_0"
        }

        but_1.setOnClickListener {
            var Last_Name_0 = editText_1.text
            textView_1.text = "This is but_1 $Last_Name_0"
        }
    }
}