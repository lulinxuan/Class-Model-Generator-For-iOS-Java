
import UIKit


class ClassA{

    var var1 = Int()
    var var2 = String()
    var time = Date()
    var isCorrect = Bool()
    var time2 = [String]()
    var time4 = Set<Date>()


    init(){}

    init(dict:Dictionary<String, String>){
        self.var1 = Int(dict["var1"]!)!
        self.var2 = dict["var2"]!
        self.time = Date(timeIntervalSince1970: Double(dict["time"]!)!)
        self.isCorrect = Bool(dict["isCorrect"]!)!
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

    func setTime(time:Date){
        self.time=time
    }

    func getTime()->Date{
        return self.time
    }

    func setIscorrect(isCorrect:Bool){
        self.isCorrect=isCorrect
    }

    func getIscorrect()->Bool{
        return self.isCorrect
    }

    func setTime2(time2:[String]){
        self.time2=time2
    }

    func getTime2()->[String]{
        return self.time2
    }

    func setTime4(time4:Set<Date>){
        self.time4=time4
    }

    func getTime4()->Set<Date>{
        return self.time4
    }

    func toDict()->Dictionary<String, String>{
        var dict = Dictionary<String, String>()
        dict["var1"] = String(self.var1)
        dict["var2"] = String(self.var2)
        dict["time"] = String(Int(self.time.timeIntervalSince1970))
        dict["isCorrect"] = String(self.isCorrect)
        return dict
    }
}
