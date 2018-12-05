using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerControl : MonoBehaviour{ 


    public float speed = 12f;
    public GameObject fallingblocks;

    void Update()
    {
        var move = new Vector3(Input.GetAxis("Horizontal"), Input.GetAxis("Vertical"), 0);
        transform.position += move * speed * Time.deltaTime;
    }


    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.name == "fallingblocks")
        {
            Destroy(collision.gameObject);
        }
    }
}
