package com.example.project_2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText

class MainActivity : AppCompatActivity() {

    lateinit var but : Button
    lateinit var editText : EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        but =  findViewById(R.id.button_0_0)
        editText = findViewById(R.id.First_Name)

        but.setOnClickListener{
            var intent:Intent = Intent(applicationContext,MainActivity2::class.java)
            var firstName = editText.text.toString()
            intent.putExtra("firstname", firstName)
            startActivity(intent)
        }
    }
}
