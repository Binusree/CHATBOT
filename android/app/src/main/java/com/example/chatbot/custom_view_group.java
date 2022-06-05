package com.example.chatbot;

import android.content.Context;
import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

public  class custom_view_group extends BaseAdapter {
    private final Context context;
    String[] gid, t, g;

    public custom_view_group(Context applicationContext, String[] t, String[] g) {

        this.context = applicationContext;
        this.t = t;
        this.g = g;

    }

    @Override
    public int getCount() {
        return t.length;
    }

    @Override
    public Object getItem(int i) {
        return null;
    }

    @Override
    public long getItemId(int i) {
        return 0;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        LayoutInflater inflator = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if (view == null) {
            gridView = new View(context);
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView = inflator.inflate(R.layout.activity_custom_view_group, null);//same class name

        } else {
            gridView = (View) view;

        }
        TextView tv1 = (TextView) gridView.findViewById(R.id.textView38);
        TextView tv2 = (TextView) gridView.findViewById(R.id.textView40);



        tv1.setTextColor(Color.RED);//color setting
        tv2.setTextColor(Color.BLACK);



        tv1.setText(t[i]);
        tv2.setText(g[i]);


//
        return gridView;

    }
}