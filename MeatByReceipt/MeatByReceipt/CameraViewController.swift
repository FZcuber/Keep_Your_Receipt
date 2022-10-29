//
//  CameraViewController.swift
//  MeatByReceipt
//
//  Created by Darren Key on 10/15/22.
//

import UIKit
import Alamofire

class CameraViewController: UIViewController{
    var imagePicker: UIImagePickerController!
    
    var imageFromPicker : UIImage?
    
    var homeTab : HomeViewController?
    
    var shouldTakePhoto = true
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        homeTab = self.tabBarController?.viewControllers?[0] as? HomeViewController
            
        takePhoto()
        // Do any additional setup after loading the view.
    }
    
    override func viewDidAppear(_ animated: Bool) {
        if shouldTakePhoto{
            takePhoto()
        }
    }
    
    func takePhoto(){
        imagePicker =  UIImagePickerController()
        imagePicker.delegate = self
        imagePicker.sourceType = .camera

        present(imagePicker, animated: true, completion: nil)
        
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
extension CameraViewController : UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
            imagePicker.dismiss(animated: true, completion: nil)
            imageFromPicker = info[.originalImage] as? UIImage
        
        
            if let imageFromPickerPngData = imageFromPicker?.pngData(){
                
                AF.upload(multipartFormData: { multipartFormData in
                    multipartFormData.append(imageFromPickerPngData, withName: "receipt", fileName: "receipt.png" , mimeType: "image/png")
                }, to: "http://34.162.217.235:5000/process/")
                .responseString(completionHandler: { [self] response in
                    print(response.value)
                    
                    print("Test if it is hit")
                    
                    homeTab?.meatWeight.text = response.value
                    
                    shouldTakePhoto = true
                    
                    self.tabBarController?.selectedIndex = 0
                })
                shouldTakePhoto = false
            }
        }

}
