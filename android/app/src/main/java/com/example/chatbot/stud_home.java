package com.example.chatbot;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.view.View;
import android.support.v4.view.GravityCompat;
import android.support.v7.app.ActionBarDrawerToggle;
import android.view.MenuItem;
import android.support.design.widget.NavigationView;
import android.support.v4.widget.DrawerLayout;

import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

public class stud_home extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    TextView t1,t2;
    ImageView im;
    SharedPreferences sh;
    String ip;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_stud_home);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        FloatingActionButton fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
//                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
//                        .setAction("Action", null).show();
                Intent i=new Intent(getApplicationContext(),chatboat_msg.class);
                startActivity(i);
            }
        });
        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        NavigationView navigationView = findViewById(R.id.nav_view);
        View headerView=navigationView.getHeaderView(0);
        t1=headerView.findViewById(R.id.t1);
        t2=headerView.findViewById(R.id.textView);
        im=headerView.findViewById(R.id.imageView);
        sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        t1.setText(sh.getString("n",""));
        t2.setText(sh.getString("e",""));
        String ip = sh.getString("ip", "");
        String url = "http://" + ip + ":5000" + sh.getString("p","");
//
        Picasso.with(getApplicationContext()).load(url).transform(new CircleTransform()).into(im);

        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();
        navigationView.setNavigationItemSelectedListener(this);
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.stud_home, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
//            return true;
            SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            SharedPreferences.Editor e=sh.edit();
            e.clear();
            e.commit();
            Intent i = new Intent(getApplicationContext(), login.class);
            i.addFlags(i.FLAG_ACTIVITY_CLEAR_TOP);
            i.addFlags(i.FLAG_ACTIVITY_NEW_TASK);
            startActivity(i);
        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_home) {
            // Handle the camera action
            Intent i =new Intent(getApplicationContext(),view_profile.class);
            startActivity(i);
        } else if (id == R.id.nav_gallery) {
            Intent i =new Intent(getApplicationContext(),view_notifications.class);
            startActivity(i);
        } else if (id == R.id.nav_slideshow) {
            Intent i =new Intent(getApplicationContext(),view_articles.class);
            startActivity(i);

        } else if (id == R.id.nav_tools) {
            Intent i =new Intent(getApplicationContext(),view_approved_evens.class);
            startActivity(i);

        } else if (id == R.id.nav_bars) {
            Intent i =new Intent(getApplicationContext(),view_ideas.class);
            startActivity(i);


        } else if (id == R.id.nav_bar) {
            Intent i =new Intent(getApplicationContext(),send_feddback.class);
            startActivity(i);


        } else if (id == R.id.nav_grp) {
            Intent i =new Intent(getApplicationContext(),view_group.class);
            startActivity(i);


//        }else if (id == R.id.nav_grpmb) {
//            Intent i =new Intent(getApplicationContext(),custom_view_group_members.class);
//            startActivity(i);


        }else if (id == R.id.nav_share) {
            Intent i = new Intent(getApplicationContext(), Chatwithstudent.class);
            startActivity(i);
        }
        else if (id == R.id.nav_send) {
            SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            SharedPreferences.Editor e=sh.edit();
            e.clear();
            e.commit();
            Intent i = new Intent(getApplicationContext(), login.class);
            i.addFlags(i.FLAG_ACTIVITY_CLEAR_TOP);
            i.addFlags(i.FLAG_ACTIVITY_NEW_TASK);
            startActivity(i);
        }


        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
