package com.example.chatbot;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class login extends AppCompatActivity {
EditText e1,e2;
Button b1;
String url;
SharedPreferences sh;
TextView t1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        e1=findViewById(R.id.editTextTextEmailAddress);
        e2=findViewById(R.id.editTextTextPassword);
        b1=findViewById(R.id.button);
        t1=findViewById(R.id.textView26);
        t1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent r = new Intent(getApplicationContext(),signup.class);
                startActivity(r);
            }
        });
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {


                final String Username=e1.getText().toString();
                final String Password=e2.getText().toString();

                int flag=0;
                if (Username.equalsIgnoreCase("")){
                    e1.setError("Enter username");
                    flag++;
                }
                if (Password.equalsIgnoreCase("")) {
                    e2.setError("Enter Password");
                    flag++;
                }
                if (flag==0){





                sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                sh.getString("ip","");
                url=sh.getString("url","")+"and_login";
                Toast.makeText(login.this, "" +url , Toast.LENGTH_SHORT).show();


                RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
                StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                        new Response.Listener<String>() {
                            @Override
                            public void onResponse(String response) {
                                  Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();

                                try {
                                    JSONObject jsonObj = new JSONObject(response);
                                    if (jsonObj.getString("status").equalsIgnoreCase("ok")) {
                                Toast.makeText(login.this, "welcome", Toast.LENGTH_SHORT).show();
                                        String typ = jsonObj.getString("type");
                                        String id = jsonObj.getString("lid");
                                        String name = jsonObj.getString("name");
                                        String email = jsonObj.getString("email");
                                        String photo = jsonObj.getString("photo");
                                        SharedPreferences.Editor ed = sh.edit();
                                        ed.putString("lid", id);
                                        ed.putString("n", name);
                                        ed.putString("e", email);
                                        ed.putString("p", photo);
                                        ed.commit();
                                        if (typ.equalsIgnoreCase("student")) {
                                            Toast.makeText(getApplicationContext(), "Welcome", Toast.LENGTH_LONG).show();
                                            Intent i = new Intent(getApplicationContext(), stud_home.class);
                                            startActivity(i);
                                        }
                                    } else {
                                        Toast.makeText(getApplicationContext(), "Not found", Toast.LENGTH_LONG).show();
                                    }

                                } catch (Exception e) {
                                    Toast.makeText(getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                                }
                            }
                        },
                        new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                // error
                                Toast.makeText(getApplicationContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
                            }
                        }
                ) {

                    //                value Passing android to python
                    @Override
                    protected Map<String, String> getParams() {
                        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                        Map<String, String> params = new HashMap<String, String>();

                        params.put("u", Username);//passing to python
                        params.put("p", Password);


                        return params;
                    }
                };


                int MY_SOCKET_TIMEOUT_MS = 100000;

                postRequest.setRetryPolicy(new DefaultRetryPolicy(
                        MY_SOCKET_TIMEOUT_MS,
                        DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                        DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
                requestQueue.add(postRequest);
                }
            }
        });



    }
}