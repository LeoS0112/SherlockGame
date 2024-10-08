//
//  ViewController.swift
//  SherlockedApp
//
//  Created by Alok Sahay on 09.03.2024.
//

import UIKit

class ViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    enum Scene {
        case lobbyScene
        case officeScene
        case gameScene
    }
    
    let sherlockView = UIImageView()
    let triggerDistance: CGFloat = 30
    var currentScene: Scene = .lobbyScene
    
    // Conversation
    
    var currentStringIndex: Int = 0
    var textTimer: Timer?
    var message: String = ""
    var dialogs: [NPCDialogue]?
    var npcs: [NPCModel]?
    
    @IBOutlet weak var conversationLabel: UILabel!
    @IBOutlet weak var dialogView: UIView!
    
    // Lobby views and environment
    
    @IBOutlet weak var plantView: UIImageView!
    @IBOutlet weak var lobbyCarpetImageView: UIImageView!
    @IBOutlet weak var lobbyView: UIView!
    @IBOutlet weak var lobbyDoorView: UIView!
    
    // Office views and environment
    
    @IBOutlet weak var officeView: UIView!
    @IBOutlet weak var watsonView: UIImageView!
    @IBOutlet weak var clientView: UIImageView!
    @IBOutlet weak var officeCarpetImage: UIImageView!
    @IBOutlet weak var officeDoorView: UIView!
    
    // game views and environment
    
    @IBOutlet weak var gameMapView: UIView!
    @IBOutlet weak var gameCarpet: UIImageView!
    @IBOutlet weak var npcView: UIImageView!
    
    // Sherlock NPC details
    let imageViewSize = CGSize(width: 80, height: 80) // Define the size as a property for easier adjustments
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupNPCs()
        startGame()
    }
    
    func setupNPCs() {
        sherlockView.frame = CGRect(x: 0, y: 0, width: imageViewSize.width, height: imageViewSize.height)
        sherlockView.layer.cornerRadius = imageViewSize.height/2
        sherlockView.image = UIImage(named: "Sherlock_default")
        sherlockView.clipsToBounds = true
        sherlockView.backgroundColor = .systemTeal
        
        watsonView.layer.cornerRadius = watsonView.frame.size.height/2
        watsonView.clipsToBounds = true
        
        showConversation(text: "You have a new case, walk to your office.")
    }
    
    func startGame() {
        moveToScene(sceneLocation: .lobbyScene)
        loadAssets()
    }
    
    func loadAssets() {
        
        // Lobby
        ContentManager.fetchAsset(assetURL: ContentManager.lobbyCarpetAssetUrl, completion: { [weak self] image, error in
            if let error = error {
                print("Error fetching image: \(error.localizedDescription)")
                return
            }
            self?.lobbyCarpetImageView.image = image
            self?.plantView.alpha = 1.0
            self?.clientView.alpha = 1.0
            self?.watsonView.alpha = 1.0
            self?.npcView.alpha = 1.0
        })
        
        // Office
        ContentManager.fetchAsset(assetURL: ContentManager.officeCarpetAssetUrl, completion: { [weak self] image, error in
            if let error = error {
                print("Error fetching image: \(error.localizedDescription)")
                return
            }
            self?.officeCarpetImage.image = image
        })
        
        // GameScene
        
        ContentManager.fetchAsset(assetURL: ContentManager.gameCarpetAssetUrl, completion: { [weak self] image, error in
            if let error = error {
                print("Error fetching image: \(error.localizedDescription)")
                return
            }
            self?.gameCarpet.image = image
        })
        
        ContentManager.getNPCs(url: ContentManager.getNPCsUrl) { [weak self] npcs, error in
            if let error = error {
                print("Error fetching npcs: \(error.localizedDescription)")
                return
            }
            self?.npcs = npcs
        }
    }
    
    func talkToWitnessNPC(completion: @escaping (NPCDialogue?, Error?) -> Void) {
        guard let witnessNPC = npcs?.max(by: { $0.npcId < $1.npcId }) else {
            completion(nil, NSError(domain: "DataError", code: 404, userInfo: nil))
            return
        }
        
        let alertController = UIAlertController(title: "Send message to: \(witnessNPC.npcName)", message: "Please enter your text below", preferredStyle: .alert)
        alertController.addTextField { textField in
            
        }
        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel)
        
        let okAction = UIAlertAction(title: "OK", style: .default) { _ in
            
            if let textField = alertController.textFields?.first, let textInput = textField.text {
                
                print("Text entered: \(textInput)")
                
                self.showConversation(text: "Sherlock: \(textInput)")
                
                ContentManager.sendConversation(url: ContentManager.sendDialogsUrl, npcId: witnessNPC.npcId, message: textInput) { dialog, error in
                    
                    if let error = error {
                        print("Error fetching response: \(error.localizedDescription)")
                        return
                    }
                    
                    completion(nil,nil)
                }
                
            }
        }
        
        alertController.addAction(cancelAction)
        alertController.addAction(okAction)
        
        // Present the alert
        present(alertController, animated: true)
        
    }
    
    func loadConversationWithClientNPC(completion: @escaping (NPCDialogue?, Error?) -> Void) {
        
        ContentManager.getConversations(url: ContentManager.getDialogsUrl) { [weak self] dialogs, error in
            if let error = error {
                print("Error fetching image: \(error.localizedDescription)")
                return
            }
            
            self?.dialogs = dialogs
            
            if let latestDialogue = dialogs?.max(by: { $0.npcDialogueID < $1.npcDialogueID }) {
                completion(latestDialogue, nil)
            } else {
                completion(nil, NSError(domain: "DataError", code: 404, userInfo: nil))
            }
        }
    }
    
    func moveToScene(sceneLocation: Scene) {
        
        if sceneLocation != currentScene {
            guard let holderView = sherlockView.superview else {
                return
            }
            holderView.gestureRecognizers?.forEach({ gesture in
                holderView.removeGestureRecognizer(gesture)
            })
            sherlockView.removeFromSuperview()
        }
        
        switch sceneLocation {
        case .lobbyScene :
            resetNPCInRoom(room: lobbyView)
            break
        case .officeScene:
            resetNPCInRoom(room: officeView)
            break
        case .gameScene:
            resetNPCInRoom(room: gameMapView)
            break
        }
        
        currentScene = sceneLocation
    }
    
    func resetNPCInRoom(room: UIView) {
        
        for room in [lobbyView,officeView,gameMapView] {
            room?.alpha = 0.3
        }
        
        room.alpha = 1.0
        
        let holderView = room
        holderView.addSubview(sherlockView)
        
        let initialLocation = CGPoint(x: self.imageViewSize.width/2, y: holderView.frame.height/2)
        sherlockView.center = initialLocation
        
        let finalLocation = CGPoint(x: holderView.frame.width/2, y: holderView.frame.height/2)
        
        UIView.animate(withDuration: 0.5) {
            self.sherlockView.center = finalLocation
        }
        
        let tapGesture = UITapGestureRecognizer(target: self, action: #selector(moveCharacter(_:)))
        holderView.addGestureRecognizer(tapGesture)
    }
    
    @objc func moveCharacter(_ gesture: UITapGestureRecognizer) {
        
        guard let holderView = sherlockView.superview else {
            return
        }
        
        showConversation(text: "")
        
        let tapLocation = gesture.location(in: holderView)
        
        // Check if theres a door in the room
        
        switch currentScene {
            
        case .lobbyScene:
            if (tapLocation.x >= holderView.bounds.width - triggerDistance) {
                // Move the imageView to the door and trigger an action
                moveSherlockToLobbyDoor()
                return
            }
        case .officeScene:
            if (tapLocation.y <= watsonView.frame.size.height + triggerDistance) {
                // move to watson
                moveSherlockToWatson()
                return
            }
            
            if (tapLocation.y >= clientView.frame.origin.y + triggerDistance) {
                // move to client
                moveSherlockToClient()
                return
            }
            
            if (tapLocation.x >= holderView.bounds.width - triggerDistance) {
                // move to office door
                moveSherlockToOfficeDoor()
                return
            }
            
        case .gameScene:
            if (tapLocation.y <= watsonView.frame.size.height + triggerDistance) {
                // move to NPC 3
                moveSherlockToWitnessNPC()
                return
            }
            
        }
        moveImageViewWithinBounds(tapLocation: tapLocation)
    }
    
    func moveImageViewWithinBounds(tapLocation: CGPoint) {
        
        guard let holderView = sherlockView.superview else {
            return
        }
        
        showConversation(text: "")
        
        var adjustedLocation = tapLocation
        
        let maxMargin = imageViewSize.width / 2
        
        adjustedLocation.x = max(tapLocation.x, maxMargin)
        adjustedLocation.x = min(tapLocation.x, holderView.bounds.width - maxMargin)
        
        adjustedLocation.y = max(tapLocation.y, maxMargin)
        adjustedLocation.y = min(tapLocation.y, holderView.bounds.height - maxMargin)
        
        UIView.animate(withDuration: 0.5) {
            self.sherlockView.center = adjustedLocation
        }
    }
    
    func moveSherlockToWatson() {
        
        UIView.animate(withDuration: 0.8) {
            self.sherlockView.center = CGPoint(x: self.watsonView.frame.origin.x, y: self.watsonView.frame.origin.y + self.imageViewSize.height / 2)
        } completion: {_ in
            self.triggerWatsonInteraction()
        }
    }
    
    func moveSherlockToClient() {
        
        UIView.animate(withDuration: 0.8) {
            self.sherlockView.center = CGPoint(x: self.watsonView.frame.origin.x, y: self.clientView.frame.origin.y + self.imageViewSize.height / 2)
        } completion: {_ in
            self.triggerClientInteraction()
        }
    }
    
    func moveSherlockToWitnessNPC() {
        
        UIView.animate(withDuration: 0.8) {
            self.sherlockView.center = CGPoint(x: self.npcView.frame.origin.x, y: self.npcView.frame.origin.y + self.imageViewSize.height / 2)
        } completion: {_ in
            self.triggerWitnessInteraction()
        }
    }
    
    
    func moveSherlockToLobbyDoor() {
        guard let holderView = sherlockView.superview else {
            return
        }
        
        UIView.animate(withDuration: 0.8) {
            self.sherlockView.center = CGPoint(x: holderView.bounds.width - self.imageViewSize.width / 2, y: self.sherlockView.center.y)
        } completion: {_ in
            self.triggerLobbyDoorAction()
        }
    }
    
    func moveSherlockToOfficeDoor() {
        guard let holderView = sherlockView.superview else {
            return
        }
        
        UIView.animate(withDuration: 0.8) {
            self.sherlockView.center = CGPoint(x: holderView.bounds.width - self.imageViewSize.width / 2, y: self.sherlockView.center.y)
        } completion: {_ in
            self.triggerOfficeDoorAction()
        }
    }
    
    @objc func triggerLobbyDoorAction() {
        print("Lobby Door triggered!")
        moveToScene(sceneLocation: .officeScene)
    }
    
    @objc func triggerOfficeDoorAction() {
        print("Lobby Door triggered!")
        moveToScene(sceneLocation: .gameScene)
    }
    
    
    @objc func triggerWatsonInteraction() {
        print("Watson triggered!")
        showConversation(text: "Dr. Watson: We have a visitor")
    }
    
    @objc func triggerClientInteraction() {
        print("Client triggered!")
        
        loadConversationWithClientNPC(completion: { [weak self] dialog, error in
            if let response = dialog?.npcResponse {
                
                self?.showConversation(text: response)
                
            }
        })
    }
    
    @objc func triggerWitnessInteraction() {
        
        
        talkToWitnessNPC { dialog, error in
            
            
            // fetch response
            DispatchQueue.main.asyncAfter(deadline: .now() + 12) { // 5 seconds delay
                // Call your function here
                self.triggerClientInteraction()
            }
        }
    }
    
    func showConversation(text: String) {
        
        message = text
        
        currentStringIndex = 0
        conversationLabel.text = ""
        textTimer?.invalidate()
        textTimer = Timer.scheduledTimer(timeInterval: 0.03, target: self, selector: #selector(updateText), userInfo: nil, repeats: true)
    }
    
    @objc func updateText() {
        
        dialogView.alpha = message.isEmpty ? 0.0 : 0.8
        
        guard currentStringIndex < message.count else {
            textTimer?.invalidate()
            return
        }
        
        let index = message.index(message.startIndex, offsetBy: currentStringIndex)
        conversationLabel.text?.append(message[index])
        currentStringIndex += 1
    }
    
    // Front camera image capture
    
    @IBAction func cameraButtonPressed(_ sender: Any) {
        captureImage()
    }
    
    func captureImage() {
        guard UIImagePickerController.isSourceTypeAvailable(.camera) else {
            print("Camera is not available.")
            return
        }
        
        let imagePicker = UIImagePickerController()
        imagePicker.sourceType = .camera
        imagePicker.cameraDevice = .front // Directly set to front camera
        imagePicker.delegate = self
        
        present(imagePicker, animated: true)
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        if let capturedImage = info[.originalImage] as? UIImage {
            
        }
        
        picker.dismiss(animated: true)
    }
    
}

