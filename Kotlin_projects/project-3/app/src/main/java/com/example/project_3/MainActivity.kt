package com.example.project_3

import android.content.Intent
import android.content.ServiceConnection
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.sax.StartElementListener
import android.widget.Button
import java.io.Serializable

class MainActivity : AppCompatActivity() {

    lateinit var but : Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        but = findViewById(R.id.button)




        but.setOnClickListener {


            val employee = Employees(firstname: "Abdallah", lastname: "El-Daly", address : "Egypt")

            startActivity(Intent(this,MainActivity2::class.java).putExtra("employee", employee))
        }

    }
}

class Employees (var firstname : String, var lastname :String, var address : String)
