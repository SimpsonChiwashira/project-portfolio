using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;
using static UnityEditor.Experimental.GraphView.GraphView;

public class RobotController : MonoBehaviour
{
    // naming constraints do not change
    [SerializeField] private WheelCollider FLWC;
    [SerializeField] private WheelCollider FRWC;
    [SerializeField] private WheelCollider BLWC;
    [SerializeField] private WheelCollider BRWC;

    [SerializeField] private Transform FLWT;
    [SerializeField] private Transform FRWT;
    [SerializeField] private Transform BLWT;
    [SerializeField] private Transform BRWT;

    [SerializeField] private Transform SFR;
    [SerializeField] private Transform SL1;
    [SerializeField] private Transform SL2;
    [SerializeField] private Transform SL3;
    [SerializeField] private Transform SR1;
    [SerializeField] private Transform SR2;
    [SerializeField] private Transform SR3;
    [SerializeField] private Transform SOR;

    [SerializeField] private float maxSteeringAngle = 30;
    private float motorForce = motorForceNrm;
    private float brakeForce;  

    [SerializeField] private float speedOfCar;

    private Rigidbody rbody;
    private float steerAngle;
    private bool isBrake;
    private float s1dist = 5;
    private float s3dist = 8f;

    private const int motorForceNrm = 20;
    private const int forwardTorqueFactorAdd = motorForceNrm / 5;

    private const  int carSpeedMaxNrm = 5;
    private const int carSpeedMaxDownhill = carSpeedMaxNrm / 2;

    private bool? ascending;

    private void Start()
    {
        rbody = GetComponent<Rigidbody>();
        //setting sensor orientation
        float s1x = 0; float s1y = 10f; float s1z = 0;
        float s2x = 8; float s2y = 27f; float s2z = 0;
        float s3x = 13; float s3y = 68; float s3z = 0;
        
        //adjusting the sensors 
        AdjustSense(SFR, 20, 0, 0);
        AdjustSense(SL1, s1x, -s1y, s1z);
        AdjustSense(SL2, s2x, -s2y, s2z);
        AdjustSense(SL3, s3x, -s3y, s3z);
        AdjustSense(SR1, s1x, s1y, s1z);
        AdjustSense(SR2, s2x, s2y, s2z);
        AdjustSense(SR3, s3x, s3y, s3z);
        AdjustSense(SOR, 0, 0, 0);

    }
    private void FixedUpdate()
    {
        //calling all functions so they are updated at any time 
        StayOnRoad();
        AvoidObstacles();
        AdjustSpeed();
        HandleMotor();
        UpdateWheels();
        
        //calculating the speed of the car
        speedOfCar = rbody.velocity.magnitude;

        float x = SOR.eulerAngles.x;

        if(x < 356f && x > 338)
        {
            ascending = true;
        }
        else if(x > 3.5f && x < 40)
        {
            ascending = false;
        }
        else
        {
            ascending = null;
        }


    }
    private void AdjustSense(Transform sensor, float x_angle, float y_angle, float z_angle)
    {
        //sensor adjustments
        sensor.transform.Rotate(x_angle, y_angle, z_angle);
    }
    private void HandleMotor()
    {
        //created a temporary local variable for motorforce 
        float tempM;
        //if the tempM is true then do not apply any brakes else apply motorForce
        tempM = isBrake ? 0 : motorForce;
        FRWC.motorTorque = tempM;
        FLWC.motorTorque = tempM;
        BLWC.motorTorque = tempM;
        BRWC.motorTorque = tempM;

        //setting the brake toque and if brake is set true then apply 3000f and stop the vehicle else dont apply any brakes.
        //brakeForce = isBrake ? 3000f : 0f;
        brakeForce = isBrake ? Mathf.Abs(Mathf.Pow(speedOfCar, 3) - motorForceNrm) : 0f;
        FLWC.brakeTorque = brakeForce;
        FRWC.brakeTorque = brakeForce;
        BLWC.brakeTorque = brakeForce;
        BRWC.brakeTorque = brakeForce;

    }
    private void UpdateWheels()
    {
        //updating the wheel colliders with the transforms
        UpdateWheelPos(FLWC, FLWT);
        UpdateWheelPos(FRWC, FRWT);
        UpdateWheelPos(BLWC, BLWT);
        UpdateWheelPos(BRWC, BRWT);
    }
    private void UpdateWheelPos(WheelCollider wheelCollider, Transform trans)
    {
        //this function is responsible for the rotation of the wheels and updates the positions.
        Vector3 pos;
        Quaternion rot;
        wheelCollider.GetWorldPose(out pos, out rot);
        trans.position = pos;
        trans.rotation = rot;

    }
    private void HandleSteer(float direction)
    {
        //this functions handles the steering, and allows the wheelcolliders to turn the vehicle to both sides given our steer angle.
        steerAngle = direction * maxSteeringAngle;
        FLWC.steerAngle = steerAngle;
        FRWC.steerAngle = steerAngle;
    }
    private bool detect(Transform sensor, float dist, LayerMask mask)   
    {
        //detecting track and obstacles layers

        //if the raycast sensor detects something the color sets to blue 
        if (Physics.Raycast(sensor.position, sensor.TransformDirection(Vector3.forward), dist, mask))
        {
            Debug.DrawRay(sensor.position, sensor.TransformDirection(Vector3.forward) * dist, Color.blue);
            return true;
        }
        else
        {
            //when the sensor doesnt detect anything the raycast sensor turns yellow
            Debug.DrawRay(sensor.position, sensor.TransformDirection(Vector3.forward) * dist, Color.yellow);
            return false;
        }
    }
    private void StayOnRoad()
    {

        isBrake = true;

        LayerMask road = LayerMask.GetMask("Road");
        bool bothInAir = !detect(SL3, s3dist, road) && !detect(SR3, s3dist, road);


        if (!detect(SL3, s3dist, road) && !bothInAir)
        {
            HandleSteer(1);
        }
        //if the right most sensor does not detect the road we steer the vehicle to the left to stay on road.
        else if (!detect(SR3, s3dist, road) && !bothInAir)
        {
            HandleSteer(-1);
        }
        else
        {
            // if the sensors detect the road then do nothing and go straight;
            isBrake = false;
            HandleSteer(0);
        }
    }
    private void AdjustSpeed()
    {
        if(speedOfCar < carSpeedMaxNrm)  // && (/* NOT GOING DOWNHILL */)
        {
            motorForce += forwardTorqueFactorAdd;
            isBrake = false;
        }
        else
        {
            motorForce = motorForceNrm;
            isBrake = true;
            // Check downhill if downhill and speed <= maxDownhill speed don't brake
        }
    }
    private void AvoidObstacles()
    {
        LayerMask mask = LayerMask.GetMask("Obstacles");

        //if the left front sensor detects an obstacle its going to steer right to avoid it
        if (detect(SL1, s1dist, mask) || detect(SL2, s1dist,mask))
        {
            HandleSteer(1);
        }
        //if the right front sensor detects the onstacle it steers the robot to the left
        if (detect(SR1, s1dist, mask) || detect(SR2, s1dist, mask))
        {
            HandleSteer(-1);
        }
    }
}