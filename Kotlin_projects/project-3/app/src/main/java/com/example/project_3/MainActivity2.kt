package com.example.project_3

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView

class MainActivity2 : AppCompatActivity() {

    lateinit var textView_0 : TextView
    lateinit var textView_1 : TextView
    lateinit var textView_2 : TextView
    lateinit var textView_3 : TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)

        textView_0 = findViewById(R.id.firstname)
        textView_1 = findViewById(R.id.lastname)
        textView_2 = findViewById(R.id.address)

        var employee = intent.getSerializableExtra("employee") as Employees
        textView_0.text = employee.firstname
        textView_1.text = employee.lastname
        textView_2.text = employee.address
    }
}