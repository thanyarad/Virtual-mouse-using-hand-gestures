# Virtual Mouse Using Hand Gestures  

This repository contains the code for a virtual mouse application that enables hands-free control of the mouse using hand gestures. Built with **OpenCV**, **Mediapipe's Hand module**, **PyAutoGUI**, and **Pynput**, the application uses real-time hand tracking to simulate mouse actions such as cursor movement, clicking, scrolling, and more.


## Features  
- **Real-time Hand Tracking**: Utilizes Mediapipe's Hand module for efficient and accurate tracking.  
- **Gesture-based Control**: Control mouse actions like:
  - Moving the cursor
  - Left-click
  - Right-click
  - Double-click
  - Screenshot  
- **Cross-Platform**: Compatible with major operating systems (Windows, macOS, and Linux).  

## Requirements  
To run the project, ensure you have the following installed:  

- Python 3.7 to 3.11  
- OpenCV  
- Mediapipe  
- PyAutoGUI  
- Pynput  

## Installation  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/your-username/virtual-mouse.git  
   cd virtual-mouse  
   ```  

2. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Run the application**:  
   ```bash  
   python v_mouse.py  
   ```

## How It Works  
1. **Hand Detection**: Mediapipe’s Hand module detects the position and landmarks of your hand in the video feed.  
2. **Mapping Gestures to Actions**: The detected gestures are mapped to corresponding mouse actions using PyAutoGUI and Pynput.  
3. **Real-time Execution**: Cursor movements and clicks are executed seamlessly, enabling intuitive interaction.  

## Future Scope  
The project has the potential for significant improvements:  
1. **Custom CNN Model**: Replace Mediapipe’s Hand module with a Convolutional Neural Network (CNN) model for hand gesture recognition.  
   - **Custom Dataset**: Train the CNN with a custom dataset of hand gestures.  
   - **Existing Dataset**: Leverage datasets like EgoHands or HandGestRec for training.  
2. **Enhanced Accuracy**: Fine-tune the model for improved accuracy in varying lighting conditions and hand orientations.  
3. **Additional Gestures**: Extend the repertoire of gestures to include more functionalities like zooming, minimizing/maximizing windows, or custom shortcuts.  
4. **Integration with AR/VR**: Utilize the technology for immersive AR/VR applications.  

---

Happy Coding! 🚀  
