using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class spawner : MonoBehaviour {

    public int playerHealth = 1;

    public Transform Spawner;
    public float spawnRate = 10f;
    public GameObject fallingblock;

    private float nextTimeToSpawn = 5f;


    void Start()
    {
        InvokeRepeating("Spawn", spawnRate, spawnRate);
    }

    void Spawn ()
    {
        Vector3 position = new Vector3(Random.Range(-7.25f, 7.25f), 13, 0);
        Instantiate(fallingblock, position, Spawner.rotation);
    }


    // Update is called once per frame





    //    void Update () {
		// if (Time.time >= nextTimeToSpawn)
        
           // Instantiate(fallingblock, new Vector3(0, 5, -1), Quaternion.identity);
           // nextTimeToSpawn = 5f;
        
	
}
