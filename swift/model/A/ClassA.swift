
import UIKit


class ClassA{

    var intVar = Int()
    var strVar = String()
    var dateVar = Date()
    var boolVar = Bool()
    var arrVar = [String]()
    var setVar = Set<Date>()


    init(){}

    init(dict:Dictionary<String, String>){
        self.intVar = Int(dict["intVar"]!)!
        self.strVar = dict["strVar"]!
        self.dateVar = Date(timeIntervalSince1970: Double(dict["dateVar"]!)!)
        self.boolVar = Bool(dict["boolVar"]!)!
        self.arrVar = dict["arrVar"]!.components(separatedBy: "#,#")
    }

    func setIntvar(intVar:Int){
        self.intVar=intVar
    }

    func getIntvar()->Int{
        return self.intVar
    }

    func setStrvar(strVar:String){
        self.strVar=strVar
    }

    func getStrvar()->String{
        return self.strVar
    }

    func setDatevar(dateVar:Date){
        self.dateVar=dateVar
    }

    func getDatevar()->Date{
        return self.dateVar
    }

    func setBoolvar(boolVar:Bool){
        self.boolVar=boolVar
    }

    func getBoolvar()->Bool{
        return self.boolVar
    }

    func setArrvar(arrVar:[String]){
        self.arrVar=arrVar
    }

    func getArrvar()->[String]{
        return self.arrVar
    }

    func setSetvar(setVar:Set<Date>){
        self.setVar=setVar
    }

    func getSetvar()->Set<Date>{
        return self.setVar
    }

    func toDict()->Dictionary<String, String>{
        var dict = Dictionary<String, String>()
        dict["intVar"] = String(self.intVar)
        dict["strVar"] = String(self.strVar)
        dict["dateVar"] = String(Int(self.dateVar.timeIntervalSince1970))
        dict["boolVar"] = String(self.boolVar)
        dict["arrVar"] = self.arrVar.joined(separator: "#,#")
        return dict
    }
}
