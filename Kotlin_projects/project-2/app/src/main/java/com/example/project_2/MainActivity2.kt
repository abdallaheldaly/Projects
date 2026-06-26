package com.example.project_2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView

class MainActivity2 : AppCompatActivity() {

    lateinit var but : Button
    lateinit var textView : TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)

        but =  findViewById(R.id.button_1_0)
        textView = findViewById(R.id.textView_1_1)
        var myintent : Intent = intent
        var myFirstName = myintent.getStringExtra("firstname")
        textView.text = myFirstName

        but.setOnClickListener{
            myintent = Intent(applicationContext,MainActivity::class.java)
            startActivity(myintent)
        }

    }
}