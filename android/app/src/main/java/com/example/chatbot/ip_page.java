package com.example.chatbot;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class ip_page extends AppCompatActivity {
    EditText e1;
    Button b1;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ip_page);
        e1=findViewById(R.id.editTextTextPersonName);
        b1=findViewById(R.id.button5);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String ip_address=e1.getText().toString();

                int flag=0;
                if (ip_address.equalsIgnoreCase("")){
                    e1.setError("Enter ip");
                    flag++;
                }
                if (flag==0) {


                    String url1 = "http://" + ip_address + ":5000/";
                    Toast.makeText(ip_page.this, "" + url1, Toast.LENGTH_SHORT).show();
                    SharedPreferences.Editor ed = sh.edit();
                    ed.putString("ip", ip_address);
                    ed.putString("url", url1);
                    ed.commit();
                    Intent i = new Intent(getApplicationContext(), login.class);
                    startActivity(i);
                }
            }


        });
    }
}