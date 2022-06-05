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

public class view_articles extends AppCompatActivity implements AdapterView.OnItemClickListener {
ListView li;
    String [] aid,t,an,a,d;
    String url;
    SharedPreferences sh;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_articles);
        li=findViewById(R.id.listview2);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        sh.getString("ip","");
        url=sh.getString("url","")+"and_viewarticles";
        Toast.makeText(view_articles.this, "" +url , Toast.LENGTH_SHORT).show();

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
                                aid= new String[js.length()];
                                t = new String[js.length()];
                                an = new String[js.length()];

                                a= new String[js.length()];
                                d = new String[js.length()];


                                for (int i = 0; i < js.length(); i++) {
                                    JSONObject u = js.getJSONObject(i);
                                    aid[i] = u.getString("article_id");//dbcolumn name in double quotes
                                    t[i] = u.getString("teacher_name");
                                    an[i] = u.getString("article_name");//dbcolumn name in double quotes

                                    a[i] = u.getString("articles");//dbcolumn name in double quotes
                                    d[i] = u.getString("date");



                                }
                                li.setAdapter(new custom_view_articles(getApplicationContext(), t,an,a, d));//custom_view_service.xml and li is the listview object


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
        final String ad=aid[i].toString();
        //Toast.makeText(this, "ok"+ad, Toast.LENGTH_SHORT).show();

        AlertDialog.Builder builder = new AlertDialog.Builder(view_articles.this);
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
                                Intent i =new Intent(getApplicationContext(),rate_articles.class);
                                i.putExtra("a",ad);
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