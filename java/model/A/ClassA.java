package model.A;

import java.io.Serializable;
import org.json.*;
import java.util.*;

public class ClassA implements Serializable{

    public ClassA(){}

    private int var1 = 0;
    private String var2 = "";
    private Date time = new Date();
    private boolean isCorrect = false;
    private List<String> time2 = new ArrayList<>();
    private Set<Date> time4 = new HashSet<>();


    public ClassA(JSONObject dict) throws JSONException{
        this.var1 = dict.getInt("var1");
        this.var2 = dict.getString("var2");
        this.time = new Date(((long)dict.getInt("time"))*1000);
        this.isCorrect = dict.getBoolean("isCorrect");
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

    public void setTime(Date time){
        this.time=time;
    }

    public Date getTime(){
        return this.time;
    }

    public void setIscorrect(boolean isCorrect){
        this.isCorrect=isCorrect;
    }

    public boolean getIscorrect(){
        return this.isCorrect;
    }

    public void setTime2(List<String> time2){
        this.time2=time2;
    }

    public List<String> getTime2(){
        return this.time2;
    }

    public void setTime4(Set<Date> time4){
        this.time4=time4;
    }

    public Set<Date> getTime4(){
        return this.time4;
    }

    public JSONObject toDict() throws JSONException{
        JSONObject dict = new JSONObject();
        dict.put("var1", String.valueOf(this.var1));
        dict.put("var2", String.valueOf(this.var2));
        dict.put("time", String.valueOf((int)(this.time.getTime()/1000)));
        dict.put("isCorrect", String.valueOf(this.isCorrect));
        return dict;
    }
}
