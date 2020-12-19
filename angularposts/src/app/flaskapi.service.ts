import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Post } from './models/post';

@Injectable({
  providedIn: 'root'
})
export class FlaskapiService {

  constructor(private httpClient: HttpClient) { }

  public server:string = "http://localhost:5000/api/";

  public getPosts() {
    return this.httpClient.get<Post>(this.server + "posts");
  }

  public getPost(postid: string) {
    return this.httpClient.get<Post>(this.server + `post/$(postid)`);
  }

  public addPost(postObj: Post, image: any) {
    console.log(postObj);
    console.log(image);

    const {title, content} = postObj;
    const formData: FormData = new FormData();

    formData.append("title", title);
    formData.append("content", content);
    formData.append("cover", image[0], image["filename"]);

    return this.httpClient.post<Post>(this.server + "addpost", formData);
  
  }
}
