export interface Post {
    id: string;
    title: string;
    text: string;
    textHTML: string;
    date: string;
}


export interface User {
    id: string
    name: string;
    photoURL: string;
}


export interface CommentAuthor extends User {}


export interface Comment {
    id: string;
    text: string;
    date: string;
    author: CommentAuthor;
    children?: Comment[];
}