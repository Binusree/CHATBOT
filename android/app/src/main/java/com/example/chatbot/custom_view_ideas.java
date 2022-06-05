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

public  class custom_view_ideas extends BaseAdapter {
    private final Context context;
    String[] iid, t, ide, d;

    public custom_view_ideas(Context applicationContext, String[] t, String[] ide, String[] d) {

        this.context = applicationContext;
        this.t = t;
        this.ide = ide;
        this.d = d;
    }

    @Override
    public int getCount() {
        return d.length;
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
            gridView = inflator.inflate(R.layout.activity_custom_view_ideas, null);//same class name

        } else {
            gridView = (View) view;

        }
        TextView tv1 = (TextView) gridView.findViewById(R.id.textView20);
        TextView tv2 = (TextView) gridView.findViewById(R.id.textView22);
        TextView tv3 = (TextView) gridView.findViewById(R.id.textView24);


        tv1.setTextColor(Color.RED);//color setting
        tv2.setTextColor(Color.BLACK);
        tv3.setTextColor(Color.BLACK);


        tv1.setText(t[i]);
        tv2.setText(ide[i]);
        tv3.setText(d[i]);

//
        return gridView;
    }
}