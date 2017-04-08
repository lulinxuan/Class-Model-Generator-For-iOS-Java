
import UIKit


class ClassC{

    var var1 = Int()
    var var2 = String()


    init(){}

    init(dict:Dictionary<String, String>){
        self.var1 = Int(dict["var1"]!)!
        self.var2 = dict["var2"]!
    }

    func setVar1(var1:Int){
        self.var1=var1
    }

    func getVar1()->Int{
        return self.var1
    }

    func setVar2(var2:String){
        self.var2=var2
    }

    func getVar2()->String{
        return self.var2
    }

    func toDict()->Dictionary<String, String>{
        var dict = Dictionary<String, String>()
        dict["var1"] = String(self.var1)
        dict["var2"] = String(self.var2)
        return dict
    }
}
