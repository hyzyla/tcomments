export interface Post {
    title: string;
    text: string;
    date: string;
}


export interface CommentAuthor {
    id: string
    name: string;
}


export interface Comment {
    id: string;
    text: string;
    date: string;
    author: CommentAuthor;
    children?: Comment[];
}