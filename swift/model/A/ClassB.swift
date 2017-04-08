
import UIKit


class ClassB{

    var var3 = Int()
    var var4 = String()


    init(){}

    init(dict:Dictionary<String, String>){
        self.var3 = Int(dict["var3"]!)!
        self.var4 = dict["var4"]!
    }

    func setVar3(var3:Int){
        self.var3=var3
    }

    func getVar3()->Int{
        return self.var3
    }

    func setVar4(var4:String){
        self.var4=var4
    }

    func getVar4()->String{
        return self.var4
    }

    func toDict()->Dictionary<String, String>{
        var dict = Dictionary<String, String>()
        dict["var3"] = String(self.var3)
        dict["var4"] = String(self.var4)
        return dict
    }
}
