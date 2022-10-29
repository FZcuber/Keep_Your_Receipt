//
//  HomeViewController.swift
//  MeatByReceipt
//
//  Created by Darren Key on 10/16/22.
//

import UIKit

class HomeViewController: UIViewController {

    @IBOutlet var containerView: UIView!
    
    
    @IBOutlet var whiteView: UIView!
    @IBOutlet var shadowView: UIView!
    @IBOutlet var meatWeight: UILabel!
    override func viewDidLoad() {
        super.viewDidLoad()
        
        whiteView.layer.cornerRadius = 15
        shadowView.layer.cornerRadius = 15
        self.tabBarController?.tabBar.isHidden = true

        // Do any additional setup after loading the view.
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
            if (segue.identifier == "StartVC") {
                let embedVC = segue.destination as! StartViewController
                embedVC.delegate = self
            }
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

protocol StartVCDelegate{
    func buttonPressed()
}


extension HomeViewController : StartVCDelegate{
    func buttonPressed() {
        
        UIView.animate(withDuration: 0.3, animations: { [self] in
            containerView.frame = CGRect(x: 0, y: -896, width: containerView.frame.width, height: containerView.frame.height)
        })
        
        self.tabBarController?.tabBar.isHidden = false
    }
}
