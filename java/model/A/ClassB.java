package model.A;

import java.io.Serializable;
import org.json.*;
import java.util.*;

public class ClassB implements Serializable{

    public ClassB(){}

    private int var3 = 0;
    private String var4 = "";


    public ClassB(JSONObject dict) throws JSONException{
        this.var3 = dict.getInt("var3");
        this.var4 = dict.getString("var4");
    }

    public void setVar3(int var3){
        this.var3=var3;
    }

    public int getVar3(){
        return this.var3;
    }

    public void setVar4(String var4){
        this.var4=var4;
    }

    public String getVar4(){
        return this.var4;
    }

    public JSONObject toDict() throws JSONException{
        JSONObject dict = new JSONObject();
        dict.put("var3", String.valueOf(this.var3));
        dict.put("var4", String.valueOf(this.var4));
        return dict;
    }
}
