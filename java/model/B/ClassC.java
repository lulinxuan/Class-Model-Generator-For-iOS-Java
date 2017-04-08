package model.B;

import java.io.Serializable;
import org.json.*;
import java.util.*;

public class ClassC implements Serializable{

    public ClassC(){}    private int var1;
    private String var2;


    public ClassC(JSONObject dict) throws JSONException{
        this.var1 = dict.getInt("var1");
        this.var2 = dict.getString("var2");
    }

    public void setVar1(int var1){
        this.var1=var1;
    }

    public int getVar1(){
        return this.var1;
    }

    public void setVar2(String var2){
        this.var2=var2;
    }

    public String getVar2(){
        return this.var2;
    }

    public JSONObject toDict() throws JSONException{
        JSONObject dict = new JSONObject();
        dict.put("var1", String.valueOf(this.var1));
        dict.put("var2", String.valueOf(this.var2));
        return dict;
    }
}
