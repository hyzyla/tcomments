export interface Post {
    id: string;
    title: string;
    text: string;
    date: string;
}


export interface CommentAuthor {
    id: string
    name: string;
    photoURL: string;
}


export interface Comment {
    id: string;
    text: string;
    date: string;
    author: CommentAuthor;
    children?: Comment[];
}