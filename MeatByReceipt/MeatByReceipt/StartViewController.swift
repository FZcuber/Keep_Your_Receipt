//
//  StartViewController.swift
//  MeatByReceipt
//
//  Created by Darren Key on 10/15/22.
//

import UIKit

class StartViewController: UIViewController {
    
    @IBOutlet var getStartedButton: UIButton!
    
    @IBOutlet var loginButton: UIButton!
    var delegate : StartVCDelegate?
    
    
    override func viewDidLoad() {
        super.viewDidLoad() 

        getStartedButton.layer.cornerRadius = 15
        loginButton.layer.cornerRadius = 15
        
        loginButton.layer.borderWidth = 1
        loginButton.layer.borderColor = UIColor.white.cgColor
        // Do any additional setup after loading the view.
    }
    

    @IBAction func getStartedPressed(_ sender: Any) {
        delegate?.buttonPressed()
    }
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
