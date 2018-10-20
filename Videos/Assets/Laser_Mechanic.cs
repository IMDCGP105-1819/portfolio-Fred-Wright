using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Laser_Mechanic : MonoBehaviour {

    public Transform firePoint;
    public GameObject bulletPrefab;


	// Update is called once per frame
	void Update () {
		if (Input.GetButtonDown("Fire1"))
        {
            Shoot();
        }
	}
    // this should be the shootey bit
    void Shoot ()
    {
        Instantiate(bulletPrefab, firePoint.position, firePoint.rotation);
    }

}
