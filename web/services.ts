import {Post, Comment, User} from "./types";


const processRequest = async (url: string, init: RequestInit | undefined = undefined) => {
    const domain = process.env.SERVER_DOMAIN || process.env.NEXT_PUBLIC_SERVER_DOMAIN;
    const resourceURL = domain ? `${domain}${url}` : url;
    const res = await fetch(resourceURL, init)
    return await res.json();
}

const getRequest = async (url: string, init: RequestInit | undefined = undefined) => {
    return await processRequest(url, init)
}

const postRequest = async (url: string, data: any) => {
    return await processRequest(url, {
        method: 'POST',
        body: JSON.stringify(data),
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        }
    })
}


export const getPost = async (postID: string): Promise<Post> => {
    return await getRequest(`/api/posts/${postID}`);
}


export const getPostComments = async (postID: string): Promise<Comment[]> => {
    return await getRequest(`/api/posts/${postID}/comments`);
}

export const getCurrentUser = async (cookie: string | null): Promise<User[]> => {
    return await getRequest(`/api/users/current`, {
        headers: {
            cookie
        },
    });
}

export const createComment = async (postID: string, text: string, parentID: string = undefined): Promise<Comment> => {
    return await postRequest(`/api/posts/${postID}/comments`, {
        text: text,
        parent_id: parentID,
    });
}