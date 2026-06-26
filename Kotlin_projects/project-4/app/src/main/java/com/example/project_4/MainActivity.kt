package com.example.project_4

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.*

class MainActivity : AppCompatActivity() {

    lateinit var listView : ListView
    lateinit var textView : TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        var personArray = arrayOf("Abdallah", "Mohamad", "El-Daly")


        listView = findViewById(R.id.listView_1)
        textView = findViewById(R.id.textView)

        listView.adapter = ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, personArray);

        listView.setOnItemClickListener{
                parent: AdapterView<*>?, view: View?, position: Int, id: Long ->

            textView.text = personArray[position]

            Toast.makeText(applicationContext, "My Name is: " +  personArray[position], Toast.LENGTH_LONG).show()
        }
    }
}
