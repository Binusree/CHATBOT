package com.example.chatbot;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class view_ideas extends AppCompatActivity implements AdapterView.OnItemClickListener{
ListView li;
    String [] iid,t,ide,d;
    String url;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_ideas);
        li=findViewById(R.id.listview1);


        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        sh.getString("ip","");
        url=sh.getString("url","")+"and_viewideas";
        Toast.makeText(view_ideas.this, "" +url , Toast.LENGTH_SHORT).show();

        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
        StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
//                        Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();

                        try {
                            JSONObject jsonObj = new JSONObject(response);
                            if (jsonObj.getString("status").equalsIgnoreCase("ok")) {

                                JSONArray js = jsonObj.getJSONArray("data");//from python
                                iid= new String[js.length()];
                                t = new String[js.length()];
                                ide = new String[js.length()];
                                d= new String[js.length()];


                                for (int i = 0; i < js.length(); i++) {
                                    JSONObject u = js.getJSONObject(i);
                                    iid[i] = u.getString("idea_id");//dbcolumn name in double quotes
                                    t[i] = u.getString("teacher_name");
                                    ide[i] = u.getString("ideas");//dbcolumn name in double quotes
                                    d[i] = u.getString("date");//dbcolumn name in double quotes



                                }
                                li.setAdapter(new custom_view_ideas(getApplicationContext(), t,ide, d));//custom_view_service.xml and li is the listview object


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
                params.put("id", sh.getString("lid", ""));//passing to python
                return params;
            }
        };


        int MY_SOCKET_TIMEOUT_MS = 100000;

        postRequest.setRetryPolicy(new DefaultRetryPolicy(
                MY_SOCKET_TIMEOUT_MS,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
        requestQueue.add(postRequest);
        li.setOnItemClickListener(this);



    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
        final String ad=iid[i].toString();
        Toast.makeText(this, "ok"+ad, Toast.LENGTH_SHORT).show();

        AlertDialog.Builder builder = new AlertDialog.Builder(view_ideas.this);
        builder.setTitle("options");
        builder.setItems(new CharSequence[]
                        {"rating","Cancel"},
                new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int which) {
                        // The 'which' argument contains the index position
                        // of the selected item
                        switch (which) {
                            case 0:

                            {
                                Intent i =new Intent(getApplicationContext(),rate_ideas.class);
                                i.putExtra("i",ad);
                                startActivity(i);
//                                requestQueue.add(postRequest);
                            }




//                            case 1:
//                            {
//
//                                RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
//                                StringRequest postRequest = new StringRequest(Request.Method.POST, url1,
//                                        new Response.Listener<String>() {
//                                            @Override
//                                            public void onResponse(String response) {
//                                                //  Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();
//
//                                                try {
//                                                    JSONObject jsonObj = new JSONObject(response);
//                                                    if (jsonObj.getString("status").equalsIgnoreCase("ok")) {
//                                                        Toast.makeText(viewpost.this, "post deleted", Toast.LENGTH_SHORT).show();
//                                                        Intent i =new Intent(getApplicationContext(),viewpost.class);
////                                                        i.putExtra("pid",id);
//                                                        startActivity(i);
//                                                    } else {
//                                                        Toast.makeText(getApplicationContext(), "Not found", Toast.LENGTH_LONG).show();
//                                                    }
//
//                                                } catch (Exception e) {
//                                                    Toast.makeText(getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
//                                                }
//                                            }
//                                        },
//                                        new Response.ErrorListener() {
//                                            @Override
//                                            public void onErrorResponse(VolleyError error) {
//                                                // error
//                                                Toast.makeText(getApplicationContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
//                                            }
//                                        }
//                                ) {
//
//                                    //                value Passing android to python
//                                    @Override
//                                    protected Map<String, String> getParams() {
//                                        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
//                                        Map<String, String> params = new HashMap<String, String>();
//
//                                        params.put("pid", id);//passing to python
//
//
//
//                                        return params;
//                                    }
//                                };
//
//
//                                int MY_SOCKET_TIMEOUT_MS = 100000;
//
//                                postRequest.setRetryPolicy(new DefaultRetryPolicy(
//                                        MY_SOCKET_TIMEOUT_MS,
//                                        DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
//                                        DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
//                                requestQueue.add(postRequest);
//
//
//                            }
                            break;

                            case 1:

                                break;


                        }
                    }
                });
        builder.create().show();
    }
}