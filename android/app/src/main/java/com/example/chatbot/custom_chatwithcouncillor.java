package com.example.chatbot;

import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;


public class custom_chatwithcouncillor extends BaseAdapter{
        private Context context;
        String[] pname1,photo1,counid;
        public custom_chatwithcouncillor(Context applicationContext, String[] pname, String[] photo, String[] councillorid) {
            this.context=applicationContext;
            this.pname1=pname;
            this.photo1=photo;
            this.counid=councillorid;
        }

        @Override
        public int getCount() {
            return photo1.length;
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
            LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

            View gridView;
            if(view==null)
            {
                gridView=new View(context);
                //gridView=inflator.inflate(R.layout.customview, null);
                gridView=inflator.inflate(R.layout.activity_custom_chatwithcouncillor,null);//same class name

            }
            else
            {
                gridView=(View)view;

            }
            TextView tv1=(TextView)gridView.findViewById(R.id.textView69);
            ImageView im=(ImageView) gridView.findViewById(R.id.imageView10);
            tv1.setTextColor( Color.BLACK);//color setting
//        tv3.setOnClickListener( new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
            SharedPreferences sh1= PreferenceManager.getDefaultSharedPreferences(context);
            SharedPreferences.Editor e1=sh1.edit();
            e1.putString( "counid",counid[i] );/////
            e1.putString( "councillorname",pname1[i] );
            e1.commit();
//                //in the case of custom page the intent

//            }
//        } );

            tv1.setText(pname1[i]);
            SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
            String ip=sh.getString("url","");
            String url=ip+photo1[i];
            Picasso.with(context).load(url).transform(new CircleTransform()). into(im);//circle





            return gridView;
        }
}
